# Generated by Django 4.1.7 on 2023-04-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0011_imagem_remove_cadastro_imagem_cadastro_imagens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='imagens',
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ManyToManyField(to='cadastro.imagem')),
            ],
        ),
    ]
