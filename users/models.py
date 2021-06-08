from django.contrib.auth import get_user_model
from django.db import models
from posts.models import Post


User = get_user_model()


class UserProfile(models.Model):
    """
    Extends the base User model.
    Allows to store additional user information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/avatar.jpg')
    viewed_posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.user.username
