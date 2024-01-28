from django.apps import AppConfig


class WatchlistAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'watchlist_app'

    def ready(self):
        # Importa el archivo de señales y ejecuta cualquier código adicional que desees aquí
        import watchlist_app.signals