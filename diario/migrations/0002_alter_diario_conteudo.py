# Generated by Django 3.2.10 on 2022-01-04 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diario',
            name='conteudo',
            field=models.TextField(max_length=500),
        ),
    ]
