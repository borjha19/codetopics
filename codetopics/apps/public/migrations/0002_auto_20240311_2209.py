# Generated by Django 3.2.12 on 2024-03-11 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleuploadedevent',
            name='article_id',
        ),
        migrations.RemoveField(
            model_name='photouploadedevent',
            name='photo_id',
        ),
        migrations.RemoveField(
            model_name='videouploadedevent',
            name='video_id',
        ),
    ]
