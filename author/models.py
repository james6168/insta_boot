from django.db import models

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(max_length=150)
    info = models.TextField()
    image = models.ImageField(upload_to="authors")
    created_at = models.DateTimeField(auto_now_add=True)

