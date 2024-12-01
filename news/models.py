from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    picture = models.ImageField(upload_to='news_pictures/')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    news_item = models.ForeignKey(NewsItem, on_delete=models.CASCADE, related_name="comments")
    picture = models.ImageField(upload_to='comment_pictures/')

    def __str__(self):
        return self.author.username + ' ' + self.content
