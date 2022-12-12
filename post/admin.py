from django.contrib import admin

# Register your models here.
from post.models import Post, Image, HashTag

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(HashTag)