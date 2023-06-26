from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    pub_date = models.DateTimeField("date published")

class Comments(models.Model):
    comment_text = models.TextField()