# Generated by Django 4.1.7 on 2023-03-31 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_delete_image_cadastro_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]