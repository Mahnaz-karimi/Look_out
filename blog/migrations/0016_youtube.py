# Generated by Django 3.2.6 on 2021-12-02 00:16

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]