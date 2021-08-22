from django.contrib.auth.models import User
from django.db import models
from hashlib import blake2b


# the 'database' of users
users = []


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # cascade er hvis user bliver slettet
    # så vil profilen bliver slettet
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  # retuneres brugernavn


class User:
    def __init__(self, name: str, password: str, email: str):
        self.name = name
        self.password = blake2b(password.encode('UTF-8')).hexdigest()
        self.email = email
        self.plan = "basic"
        self.reset_code = ""

    def __repr__(self):
        return f"NAME: {self.name}, EMAIL: {self.email}, PASSWD: {self.password}"

    def reset_password(self, code: str, new_password: str):
        if code != self.reset_code:
            raise Exception("Invalid password reset code.")
        self.password = blake2b(new_password.encode('UTF-8')).hexdigest()


# stub methods for actions related to creating a new user


def create_user(name: str, password: str, email: str):
    print(f"DB: creating user database entry for {name} ({email}).")
    new_user = User(name, password, email)
    users.append(new_user)
    return new_user


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