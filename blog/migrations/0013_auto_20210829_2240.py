# Generated by Django 3.1.7 on 2021-08-29 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210810_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['id']},
        ),
    ]
