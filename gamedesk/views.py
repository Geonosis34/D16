from django.shortcuts import redirect, render

from .models import *
from django.views.generic import *
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .forms import *
from .utils.permissions import IsAuthorMixin, NotIsAuthorMixin


class PostList(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.order_by('-dateCreation')

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post_detail'
    template_name = 'gamedesk/post_detail.html'

    #def get_absolut_url(self):
        #return reverse('post_detail', kwargs={'pk': self.pk})


class PostCreate(PermissionRequiredMixin, CreateView):
    template_name = 'gamedesk/post_add.html'
    form_class = PostForm
    context_object_name = 'post_create'
    model = Post
    permission_required = ('post.post_add', )


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


class CommentsList(IsAuthorMixin, View):
    def get(self, request, *args, **kwargs):
        post_pk = kwargs['post_pk']
        post = Post.objects.get(pk=post_pk)
        qs = Comment.objects.order_by('dateCreation').filter(post=post)

        context = {
            'comments': qs,
            'post': post
        }

        return render(request, 'gamedesk/comment_list.html', context)

class CommentCreate(NotIsAuthorMixin, View):
    def get(self, request, **kwargs):
        form = CommentCreateForm(request.POST or None)
        post = Post.objects.get(pk=kwargs['post_pk'])

        context = {
            'form': form,
            'post': post
        }

        return render(request, 'gamedesk/comment_create.html', context)

    def post(self, request, *args, **kwargs):
        form = CommentCreateForm(request.POST)
        user = request.user
        post_pk = kwargs['post_pk']

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = user
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()

        return redirect('post_list')


class CommentAccept(IsAuthorMixin, View):
    def get(self, request, *args, **kwargs):
        comment_pk = kwargs['comment_pk']

        comment = Comment.objects.get(pk=comment_pk)
        comment.approved = True
        comment.save()

        return redirect(request.META['HTTP_REFERER'])


class CommentReject(IsAuthorMixin, View):
    def get(self, request, *args, **kwargs):
        comment_pk = kwargs['comment_pk']

        comment = Comment.objects.get(pk=comment_pk)
        comment.approved = False
        comment.save()

        return redirect(request.META['HTTP_REFERER'])


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'gamedesk/comment_delete.html'
    success_url = '/gamedesk/'
    permission_required = ('gamedesk.comment_delete')
    context_object_name = 'comment'

    def get_object(self, **kwargs ):
        comment_id = self.kwargs.get('comment_pk')
        comment = Comment.objects.get(pk=comment_id)
        return comment

class ByAuthorView(ListView):
    def get(self, request, *args, **kwargs):
      author = User.objects.get(username=kwargs['name'])
      qs = Post.objects.order_by('-dateCreation').filter(author = author)

      context = {
          'author': author,
          'posts': qs,
      }

      return render(request, 'gamedesk/by_author.html', context)


class CategoryView(ListView):
    def get(self, request, *args, **kwargs):
      category = Category.objects.get(name=kwargs['name'])
      qs = Post.objects.order_by('-dateCreation').filter(category = category)

      context = {
          'category': category,
          'posts': qs,

      }

      return render(request, 'gamedesk/category_list.html', context)