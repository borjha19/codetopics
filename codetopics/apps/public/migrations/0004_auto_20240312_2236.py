# Generated by Django 3.2.12 on 2024-03-12 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20240312_2236'),
        ('public', '0003_auto_20240312_2220'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArticleUploadedEvent',
        ),
        migrations.DeleteModel(
            name='PhotoUploadedEvent',
        ),
        migrations.DeleteModel(
            name='VideoUploadedEvent',
        ),
    ]