# Generated by Django 3.2.6 on 2021-12-02 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_alter_photo_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='author',
        ),
    ]
