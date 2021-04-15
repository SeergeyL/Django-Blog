from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class UserProfile(models.Model):
    """
    Extends the base User model.
    Allows to store user avatars.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/avatar.jpg')

    def __str__(self):
        return self.user.username