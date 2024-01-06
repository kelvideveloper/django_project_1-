# Generated by Django 5.0 on 2024-01-03 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0009_remove_aluno_cidade_remove_aluno_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='crupo_de_atendimento',
            field=models.IntegerField(choices=[(None, 'Pessoas acima de 75 anos'), (None, 'Pessoas entre 60 a 74 anos'), (None, 'Forças de Segurança e Salvamento'), ('001401', 'Funcionário do Sistema de Privação de Liberdade'), (None, 'Trabalhadores da Saúde'), ('000301', 'Pessoas acima de 60 anos institucionalizadas'), ('001201', 'Pessoas em Situação de Rua'), (None, 'Trabalhadores da educação'), ('001002', 'Caminhoneiro'), ('001301', 'Trabalhadores Portuários'), ('000201', 'Pessoas de 60 a 64 anos'), ('000202', 'Pessoas de 65 a 69 anos'), ('000203', 'Pessoas de 70 a 74 anos'), ('000204', 'Pessoas de 75 a 79 anos'), ('000205', 'Pessoas de 80 anos ou mais'), ('000110', 'Síndrome de Down'), ('000401', 'Marinha do Brasil - MB'), ('000402', 'Exército Brasileiro - EB'), ('000403', 'Força Aérea Brasileira - FAB'), ('000501', 'Bombeiro Civil'), ('000502', 'Bombeiro Militar'), ('000503', 'Guarda Municipal'), ('000504', 'Policial Rodoviário Federal'), ('000505', 'Policial Civil'), ('000506', 'Policial Federal'), ('000507', 'Policial Militar'), ('000601', 'Quilombola'), ('000701', 'Povos indígenas em terras indígenas'), ('000801', 'Ensino Básico'), ('000802', 'Ensino Superior'), ('000901', 'Auxiliar de Veterinário'), ('000902', 'Biólogo'), ('000903', 'Biomédico'), ('000904', 'Cozinheiro e Auxiliares'), ('000905', 'Cuidador de Idosos'), ('000906', 'Doula/Parteira'), ('000907', 'Enfermeiro(a)'), ('000908', 'Farmacêutico'), ('000909', 'Fisioterapeutas'), ('000910', 'Fonoaudiólogo'), ('000911', 'Funcionário do Sistema Funerário que tenham contato com cadáveres potencialmente contaminados'), ('000912', 'Médico'), ('000913', 'Médico Veterinário'), ('000914', 'Motorista de Ambulância'), ('000915', 'Nutricionista'), ('000916', 'Odontologista'), ('000917', 'Pessoal da Limpeza'), ('000918', 'Profissionais de Educação Física'), ('000919', 'Psicólogo'), ('000920', 'Recepcionista'), ('000921', 'Segurança'), ('000922', 'Assistente Social'), ('000923', 'Técnico de Enfermagem'), ('000924', 'Técnico de Veterinário'), ('000925', 'Terapeuta Ocupacional'), ('000926', 'Outros'), ('000927', 'Auxiliar de Enfermagem'), ('000928', 'Técnico de Odontologia'), ('000929', 'Estudante'), ('001001', 'Aéreo'), ('001003', 'Coletivo Rodoviário Passageiros Urbano e de Longo Curso'), ('001004', 'Ferroviário'), ('001005', 'Metroviário'), ('001006', 'Aquaviário'), ('001101', 'Pessoas com Deficiência Institucionalizadas'), ('001102', 'Pessoas com Deficiências Permanente Grave'), ('001501', 'População Privada de Liberdade'), ('001601', 'Trabalhadores Industriais'), ('000204', 'Pessoas ACAMADAS de 75 a 79'), ('000205', 'Pessoas ACAMADAS de 80 anos ou mais')]),
        ),
    ]
