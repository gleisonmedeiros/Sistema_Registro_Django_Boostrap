# Generated by Django 4.1.7 on 2023-03-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_cadastro_destino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='data_do_processo',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='data_do_recebimento',
            field=models.DateField(null=True),
        ),
    ]
