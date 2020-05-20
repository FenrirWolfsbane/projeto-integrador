# Generated by Django 3.0.6 on 2020-05-19 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_remove_paciente_telefone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='data_nascimento',
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='telefone'),
        ),
    ]