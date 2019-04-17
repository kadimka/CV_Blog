from django.contrib import admin
from .models import Post, Comment, Task

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Task)

# Register your models here.
