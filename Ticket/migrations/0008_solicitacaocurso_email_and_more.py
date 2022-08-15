# Generated by Django 4.0.4 on 2022-08-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0007_alter_solicitacaocurso_capacitacao_interlocutores_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacaocurso',
            name='email',
            field=models.EmailField(default='email@email.com', max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitacaodisciplina',
            name='grupos',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Grupos (ex.: AB, C, ...)'),
        ),
        migrations.AlterField(
            model_name='solicitacaodisciplina',
            name='turma',
            field=models.CharField(max_length=12, verbose_name='Turmas pelas quais sou responsável'),
        ),
    ]