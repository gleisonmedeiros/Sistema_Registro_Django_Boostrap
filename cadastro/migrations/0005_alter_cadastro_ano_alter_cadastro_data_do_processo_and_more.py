# Generated by Django 4.1.7 on 2023-03-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_cadastro_ano_alter_cadastro_numero_do_processo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='ano',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='data_do_processo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='data_do_recebimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='destino',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='numero_do_processo',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='responsavel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
