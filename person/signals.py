from django.db.models.signals import post_save
from django.contrib.auth.models import User  # hvem som sender signal
from django.dispatch import receiver
from person.models import Profile


@receiver(post_save, sender=User)  # argument er en signal for gemme og en user.
def create_profile(sender, instance, created, **kwargs):
    if created:  # Hver gang created-metode for at oprette en user er blevet brugt,
        # så vil der laves en profile med det samme
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):  # ** undtager hver ekstra tegn som sendes fra keyword
    instance.profile.save()   # Profilen bliver gemt