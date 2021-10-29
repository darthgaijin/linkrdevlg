from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import uuid
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    firstName = models.CharField(max_length=200, blank=False, null=False)
    lastName = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=500, blank=False, null=False)
    username = models.CharField(max_length=200, blank=True, null=True, unique=True)
    userStatus = models.CharField(max_length=200, blank=True, null=True, default='New user')
    profileImage = models.ImageField(blank=True, null=True, upload_to='images/user/', default='images/user/user-default.png')
    socialTitle1 = models.CharField(max_length=200, blank=True, null=True)
    socialLink1 = models.URLField(max_length=200, blank=True, null=True)
    socialTitle2 = models.CharField(max_length=200, blank=True, null=True)
    socialLink2 = models.URLField(max_length=200, blank=True, null=True)
    socialTitle3 = models.CharField(max_length=200, blank=True, null=True)
    socialLink3 = models.URLField(max_length=200, blank=True, null=True)
    socialTitle4 = models.CharField(max_length=200, blank=True, null=True)
    socialLink4 = models.URLField(max_length=200, blank=True, null=True)
    socialTitle5 = models.CharField(max_length=200, blank=True, null=True)
    socialLink5 = models.URLField(max_length=200, blank=True, null=True)
    isOwner = models.BooleanField(default=False)
    isDonator = models.BooleanField(default=False)
    isSuperDonator = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
    isNewUser = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profileImage.path)

        if img.height > 600 or img.width > 600:
            outputSize = (300, 300)
            img.thumbnail(outputSize)
            img.save(self.profileImage.path)
        elif img.height < 300 or img.width < 300:
            outputSize = (300, 300)
            img.thumbnail(outputSize)
            img.save(self.profileImage.path)


    def __str__(self):
        return f'User: [ {self.username} ] | Email: [ {self.email} ] '
