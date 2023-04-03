# Generated by Django 4.1.7 on 2023-03-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_alter_cadastro_ano_alter_cadastro_data_do_processo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='cadastro',
            name='images',
            field=models.ManyToManyField(to='cadastro.image'),
        ),
    ]