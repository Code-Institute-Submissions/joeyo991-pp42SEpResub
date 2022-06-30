from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# The User Profile Model
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username
