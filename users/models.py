from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='pictures', default=os.path.join('pictures', 'spade.png'))

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height > 200 or img.width > 200:
            img.thumbnail((200, 200))
            img.save(self.profile_pic.path)
