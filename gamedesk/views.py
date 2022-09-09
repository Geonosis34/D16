from .models import *
from django.views.generic import *


class PostList(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.order_by('-dateCreation')
