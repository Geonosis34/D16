from .models import *
from django.views.generic import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import PostForm


class PostList(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.order_by('-dateCreation')

class PostDetail(DetailView):
    model = Post
    template_name = 'gamedesk/post_detail.html'
    context_object_name = 'post_detail'

class PostCreate(PermissionRequiredMixin, CreateView):
    template_name = 'gamedesk/post_add.html'
    form_class = PostForm
    context_object_name = 'post_create'
    model = Post
    permission_required = ('post.post_add', )

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'gamedesk/post_add.html'
    permission_required = ('post.post_update',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'gamedesk/post_delete.html'
    success_url = '/gamedesk/'
    queryset = Post.objects.all()
    permission_required = ('post.post_delete',)

