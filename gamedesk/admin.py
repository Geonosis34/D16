from django.contrib import admin

from .forms import PostForm
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm

#admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)