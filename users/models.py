from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from io import BytesIO
from PIL import Image
import os

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='pictures', default=os.path.join('pictures', 'spade.png'))

    # below is how we first set up profile image. it works but need to change it up
    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.profile_pic.path)

    #     if img.height > 200 or img.width > 200:
    #         img.thumbnail((200, 200))
    #         img.save(self.profile_pic.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        memfile = BytesIO()

        img = Image.open(self.profile_pic)
        if img.height > 1000 or img.width > 1000:
            output_size = (200, 200)
            img.thumbnail(output_size, Image.ANTIALIAS)
            img.save(memfile, 'JPEG', quality=95)
            default_storage.save(self.profile_pic.name, memfile)
            memfile.close()
            img.close
