# Generated by Django 4.0.4 on 2022-08-23 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Acesso_Restrito', '0008_alter_cm_pessoa_documentacao_cidade_nascimento'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CM_cidade',
        ),
    ]