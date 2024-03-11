from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.apps import apps


class PublicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'codetopics.apps.public'


