# Generated by Django 4.0.1 on 2022-02-06 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loadimage', '0002_alter_tablaarchivo_url_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablaarchivo',
            name='url_img',
            field=models.CharField(max_length=100),
        ),
    ]
