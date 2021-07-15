from django.db.models.signals import post_save
from django.contrib.auth.models import User  # hvsm som sender signal
from django.dispatch import receiver# person som får signal
from .models import Profile


@receiver(post_save, sender=User) # som argument for en der får signal og en anden som sender signal og det er receiver som creat en profile
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User) # efter at skab en profil så vil gemmes med den methode
def save_profile(sender, instance, **kwargs): # **kwargs undtager hver ekstra tegn til funktion
    instance.profile.save()# instance er user