import json
import urllib
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.contrib.admin.options import get_content_type_for_model
from django.core.management.base import BaseCommand
from web.datasets.models import File, TCMBADocument
from web.datasets.parsers import from_str_to_date
from web.datasets.services import get_s3_client

client = get_s3_client(settings)


def extract_params(s3_filepath):
    """Extrai mês, ano e periodicidade do caminho do bucket."""
    prefix = "tcmbapublicconsultation/"
    start_index = s3_filepath.find(prefix) + len(prefix)
    relative_path = Path(s3_filepath[start_index:])
    folders = relative_path.parts
    year = folders[0]
    period = folders[1]
    month = None
    if period == "mensal":
        month = folders[2]
    return {"year": year, "period": period, "month": month}


def build_s3_path(s3_filepath, unit, category, filename):
    """
    Input:
    maria-quiteria/files/tcmbapublicconsultation/2020/mensal/12/consulta-publica-12-2020.json

    Output:
    s3://dadosabertosdefeira/maria-quiteria/files/tcmbapublicconsultation/2020/mensal/12/<unit>/<category>/<filename>
    """
    prefix = "s3://dadosabertosdefeira/"
    parts = s3_filepath.split("/")
    parts.pop()  # remove json da lista
    parts.extend([unit, category, filename])
    return f"{prefix}{'/'.join(parts)}"


def build_s3_url(s3_filepath):
    """
    Input:
    maria-quiteria/files/tcmbapublicconsultation/2020/mensal/12/<unit>/<category>/<filename>

    Output:
    https://dadosabertosdefeira.s3.eu-central-1.amazonaws.com/
    maria-quiteria/files/tcmbapublicconsultation/2020/mensal/12/<unit>/<category>/<filename>
    """
    s3_url = "https://dadosabertosdefeira.s3.eu-central-1.amazonaws.com/"
    return urllib.parse.quote_plus(f"{s3_url}{s3_filepath}")


def get_original_filename(item):
    if item.get("original_filename"):
        return item["original_filename"]
    else:
        # exemplo: 1a35fd41-e463-488a-936e-a526d3afa72a-OF\u00cdCIO.pdf
        uuid4_len = 36
        return item["filename"][uuid4_len + 1 :]


class Command(BaseCommand):
    help = "Importa documentos do TCM-BA em um bucket S3."

    def add_arguments(self, parser):
        parser.add_argument("s3_path")
        parser.add_argument("--drop-all", action="store_true")

    def echo(self, text, style=None):
        self.stdout.write(style(text) if style else text)

    def warn(self, text):
        return self.echo(text, self.style.WARNING)

    def success(self, text):
        return self.echo(text, self.style.SUCCESS)

    def handle(self, *args, **options):
        self.echo(f"Caminho no S3: {options.get('s3_path')}")
        params = extract_params(options.get("s3_path"))

        file_items = client.download_file(options.get("s3_path"))
        json_items = json.loads(open(file_items).read())

        public_view_url = "https://e.tcm.ba.gov.br/epp/ConsultaPublica/listView.seam"

        if options.get("drop_all"):
            confirmation = input("Apagar todos os arquivos do TCM-BA? s/n ")
            if confirmation.lower() in ["s", "y"]:
                TCMBADocument.objects.all().delete()

        for item in json_items:
            self.echo(str(item))
            s3_file_path = build_s3_path(
                options.get("s3_path"), item["unit"], item["category"], item["filename"]
            )
            s3_url = build_s3_url(options.get("s3_path"))

            document, _ = TCMBADocument.objects.get_or_create(
                year=params["year"],
                month=params["month"],
                period=params["period"],
                category=item["category"],
                unit=item["unit"],
                inserted_at=from_str_to_date(item["inserted_at"]),
                inserted_by=item["inserted_by"],
                original_filename=get_original_filename(item),
                crawled_at=datetime.fromisoformat(item["crawled_at"]),
                crawled_from=public_view_url,
            )
            content_type = get_content_type_for_model(document)
            File.objects.get_or_create(
                url=public_view_url,
                content_type=content_type,
                object_id=document.pk,
                s3_url=s3_url,
                s3_file_path=s3_file_path,
            )
