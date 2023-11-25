from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
# Create your models here.
