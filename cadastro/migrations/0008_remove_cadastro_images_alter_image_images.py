# Generated by Django 4.1.7 on 2023-03-31 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_rename_image_image_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='images',
        ),
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.FileField(upload_to='images/'),
        ),
    ]
