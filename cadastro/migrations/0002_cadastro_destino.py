# Generated by Django 4.1.7 on 2023-03-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='destino',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
