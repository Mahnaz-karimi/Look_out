from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):  #  appen vil bruge signal for at oprette en profile når en user er added
        import blog.signals as signal
        print(signal)
