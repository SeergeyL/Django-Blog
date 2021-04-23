from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey('PostCategory', on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    image = models.ImageField(upload_to='posts/', default='posts/default.jpg')

    def __str__(self):
        return self.text[:10]


class PostCategory(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text[:10]


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')