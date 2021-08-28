from django.contrib.auth.models import User
from django.db import models

# the 'database' of users
users = []


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # cascade er hvis user bliver slettet
    # så vil profilen bliver slettet
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  # retuneres brugernavn


def find_user(email: str):
    for user in users:
        if user.email == email:
            return user
    raise Exception(f"User with email address {email} not found.")


'''
    
    def save(self, *args, **kwargs):  # Den del bliver tilføjet for at resize billede
        super(Profile, self).save(*args, **kwargs)
        # added **kwargs for at undgå fejlen: 'force_insert'
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
'''