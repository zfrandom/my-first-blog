from django.contrib import admin
from .models import Post, Comment
# Register your models here.
admin.site.register(Post) #make the model visible on the admin page
admin.site.register(Comment)

