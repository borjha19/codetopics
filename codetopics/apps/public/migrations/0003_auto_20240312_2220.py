# Generated by Django 3.2.12 on 2024-03-12 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20240311_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleuploadedevent',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='photouploadedevent',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='videouploadedevent',
            name='url',
            field=models.URLField(null=True),
        ),
    ]