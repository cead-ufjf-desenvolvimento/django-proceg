# Generated by Django 4.0.4 on 2022-08-25 17:01

from django.db import migrations, models
import procead.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0002_alter_cm_curso_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='si_curso_oferta',
            name='ano_oferta',
            field=models.PositiveIntegerField(default=2022, validators=[procead.validators.validate_edital_year], verbose_name='Ano'),
            preserve_default=False,
        ),
    ]