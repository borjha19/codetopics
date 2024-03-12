# Generated by Django 3.2.12 on 2024-03-12 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20240311_2209'),
        ('accounts', '0002_auto_20240310_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='articles',
            field=models.ManyToManyField(blank=True, to='public.ArticleUploadedEvent'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(blank=True, to='accounts.Interest'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photos',
            field=models.ManyToManyField(blank=True, to='public.PhotoUploadedEvent'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='videos',
            field=models.ManyToManyField(blank=True, to='public.VideoUploadedEvent'),
        ),
    ]