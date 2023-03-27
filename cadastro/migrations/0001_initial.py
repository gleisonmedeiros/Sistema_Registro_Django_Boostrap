# Generated by Django 4.1.7 on 2023-03-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requerente', models.CharField(max_length=100)),
                ('assunto', models.CharField(max_length=100)),
                ('numero_do_processo', models.CharField(max_length=15)),
                ('ano', models.IntegerField()),
                ('data_do_processo', models.DateField()),
                ('data_do_recebimento', models.DateField()),
                ('responsavel', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]