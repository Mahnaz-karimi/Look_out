from django.apps import AppConfig


class PersonConfig(AppConfig):
    name = 'person'

    def ready(self):  # gøre at signal.py bliver klaret til at opload default billede
        import person.signals as signal
        print(signal)
