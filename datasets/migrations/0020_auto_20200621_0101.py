# Generated by Django 3.0.7 on 2020-06-21 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0019_auto_20200620_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citycouncilagenda',
            name='event_type',
            field=models.CharField(blank=True, choices=[('sessao_ordinaria', 'Sessão Ordinária'), ('ordem_do_dia', 'Ordem do Dia'), ('sessao_solene', 'Sessão Solene'), ('sessao_especial', 'Sessão Especial'), ('audiencia_publica', 'Audiência Pública')], db_index=True, max_length=20, null=True, verbose_name='Tipo do evento'),
        ),
        migrations.AlterField(
            model_name='citycouncilattendancelist',
            name='council_member',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Vereador'),
        ),
        migrations.AlterField(
            model_name='citycouncilattendancelist',
            name='status',
            field=models.CharField(choices=[('presente', 'Presente'), ('falta_justificada', 'Falta Justificada'), ('licenca_justificada', 'Licença Justificada'), ('ausente', 'Ausente')], db_index=True, max_length=20, verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='citycouncilbid',
            name='code',
            field=models.CharField(db_index=True, max_length=15, verbose_name='Código da licitação'),
        ),
        migrations.AlterField(
            model_name='citycouncilbid',
            name='code_type',
            field=models.CharField(db_index=True, max_length=15, verbose_name='Código do tipo da licitação'),
        ),
        migrations.AlterField(
            model_name='citycouncilbid',
            name='description',
            field=models.TextField(db_index=True, verbose_name='Descrição (objeto)'),
        ),
        migrations.AlterField(
            model_name='citycouncilbid',
            name='external_code',
            field=models.CharField(db_index=True, max_length=10, verbose_name='Código externo'),
        ),
        migrations.AlterField(
            model_name='citycouncilbid',
            name='modality',
            field=models.CharField(blank=True, choices=[('tomada_de_precos', 'Tomada de Preço'), ('pregao_presencial', 'Pregão Presencial'), ('pregao_eletronico', 'Pregão Eletrônico'), ('leilao', 'Leilão'), ('inexigibilidade', 'Inexigibilidade'), ('dispensada', 'Dispensada'), ('convite', 'Convite'), ('concurso', 'Concurso'), ('concorrencia', 'Concorrência'), ('chamada_publica', 'Chamada Pública')], db_index=True, max_length=60, null=True, verbose_name='Modalidade'),
        ),
        migrations.AlterField(
            model_name='citycouncilbid',
            name='session_at',
            field=models.DateTimeField(db_index=True, null=True, verbose_name='Sessão Data / Horário'),
        ),
        migrations.AlterField(
            model_name='citycouncilcontract',
            name='company_or_person',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Empresa ou pessoa'),
        ),
        migrations.AlterField(
            model_name='citycouncilcontract',
            name='company_or_person_document',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='CNPJ ou CPF'),
        ),
        migrations.AlterField(
            model_name='citycouncilcontract',
            name='description',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='citycouncilcontract',
            name='details',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Objeto do contrato'),
        ),
        migrations.AlterField(
            model_name='citycouncilcontract',
            name='end_date',
            field=models.DateField(db_index=True, verbose_name='Data final'),
        ),
        migrations.AlterField(
            model_name='citycouncilcontract',
            name='external_code',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Código externo'),
        ),
        migrations.AlterField(
            model_name='citycouncilcontract',
            name='start_date',
            field=models.DateField(db_index=True, verbose_name='Data de início'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='company_or_person',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Empresa ou pessoa'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='date',
            field=models.DateField(db_index=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='document',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='CNPJ ou CPF'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='external_file_code',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Código do arquivo (externo)'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='external_file_line',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Linha do arquivo (externo)'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='function',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Função'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='group',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Grupo'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='legal_status',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='Natureza'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='modality',
            field=models.CharField(blank=True, choices=[('convenio', 'Convênio'), ('tomada_de_precos', 'Tomada de Preço'), ('pregao', 'Pregão'), ('inexigibilidade', 'Inexigibilidade'), ('convite', 'Convite'), ('concorrencia', 'Concorrência'), ('dispensa', 'Dispensa'), ('isento', 'Isento')], db_index=True, max_length=50, null=True, verbose_name='Modalidade'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='number',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='phase',
            field=models.CharField(choices=[('empenho', 'Empenho'), ('liquidacao', 'Liquidação'), ('pagamento', 'Pagamento')], db_index=True, max_length=20, verbose_name='Fase'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='phase_code',
            field=models.CharField(blank=True, db_index=True, max_length=20, null=True, verbose_name='Código da fase'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='process_number',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Número do processo'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='published_at',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='Publicado em'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='resource',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='Fonte'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='subfunction',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Subfunção'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='subgroup',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Subgrupos'),
        ),
        migrations.AlterField(
            model_name='citycouncilexpense',
            name='summary',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='citycouncilminute',
            name='date',
            field=models.DateField(db_index=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='citycouncilminute',
            name='event_type',
            field=models.CharField(blank=True, choices=[('sessao_ordinaria', 'Sessão Ordinária'), ('ordem_do_dia', 'Ordem do Dia'), ('sessao_solene', 'Sessão Solene'), ('sessao_especial', 'Sessão Especial'), ('audiencia_publica', 'Audiência Pública')], db_index=True, max_length=20, null=True, verbose_name='Tipo de evento'),
        ),
        migrations.AlterField(
            model_name='citycouncilminute',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='cityhallbid',
            name='codes',
            field=models.CharField(db_index=True, max_length=300, verbose_name='Códigos'),
        ),
        migrations.AlterField(
            model_name='cityhallbid',
            name='description',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='cityhallbid',
            name='modality',
            field=models.CharField(blank=True, choices=[('tomada_de_precos', 'Tomada de Preço'), ('pregao_presencial', 'Pregão Presencial'), ('pregao_eletronico', 'Pregão Eletrônico'), ('leilao', 'Leilão'), ('inexigibilidade', 'Inexigibilidade'), ('dispensada', 'Dispensada'), ('convite', 'Convite'), ('concurso', 'Concurso'), ('concorrencia', 'Concorrência'), ('chamada_publica', 'Chamada Pública')], db_index=True, max_length=60, null=True, verbose_name='Modalidade'),
        ),
        migrations.AlterField(
            model_name='cityhallbid',
            name='public_agency',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Órgão'),
        ),
        migrations.AlterField(
            model_name='cityhallbid',
            name='session_at',
            field=models.DateTimeField(db_index=True, null=True, verbose_name='Sessão Data / Horário'),
        ),
        migrations.AlterField(
            model_name='cityhallbidevent',
            name='summary',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='file',
            name='object_id',
            field=models.PositiveIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='url',
            field=models.URLField(db_index=True, verbose_name='Arquivo'),
        ),
        migrations.AlterField(
            model_name='gazette',
            name='date',
            field=models.DateField(db_index=True, null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='gazette',
            name='power',
            field=models.CharField(choices=[('executivo', 'Poder Executivo'), ('legislativo', 'Poder Legislativo')], db_index=True, max_length=25, verbose_name='Poder'),
        ),
        migrations.AlterField(
            model_name='gazette',
            name='year_and_edition',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Ano e edição'),
        ),
        migrations.AlterField(
            model_name='gazetteevent',
            name='secretariat',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Secretaria'),
        ),
        migrations.AlterField(
            model_name='gazetteevent',
            name='summary',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Sumário'),
        ),
        migrations.AlterField(
            model_name='gazetteevent',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='Título'),
        ),
    ]
