from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published')
    ]

    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.blog.title}'


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='likes', on_delete=models.CASCADE)
    likes = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.blog.title}'


class PostViews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post_views = models.PositiveIntegerField(default=0)
    blog = models.ForeignKey(Blog, related_name='blogView', on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.blog.title} viewed by {self.user.username}'




