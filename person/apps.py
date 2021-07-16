from django.apps import AppConfig


class PersonConfig(AppConfig):
    name = 'person'

    def ready(self):  # appen vil bruge signal for at oprette en profile når en user er added
        import person.signals as signal
        print(signal)
