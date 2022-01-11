from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Post
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


@receiver(post_save, sender=Post)
def notify_users(sender, instance, created, **kwargs):
    if created:
        users = User.objects.all()
        for user in users:
            send_mail('Hello from Mahnaz', 'Hello there. this is an automate message. There are som new post',
                      settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

