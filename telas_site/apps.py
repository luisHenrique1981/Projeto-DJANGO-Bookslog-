from django.apps import AppConfig


class TelasSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telas_site'

    def ready(self):
        import telas_site.signals
