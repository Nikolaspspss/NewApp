from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post
from django.http import HttpResponse
from .filters import PostFilter
from .forms import PostForm




class PostList(ListView):
    model = Post
    template_name = 'News.html'
    context_object_name = 'Post'
    paginate_by = 10

    def get_queryset(self):

        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset

        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'News2.html'
    context_object_name = 'Post'
    paginate_by = 1


def multiply(request):
   number = request.GET.get('number')
   multiplier = request.GET.get('multiplier')

   try:
       result = int(number) * int(multiplier)
       html = f"<html><body>{number}*{multiplier}={result}</body></html>"
   except (ValueError, TypeError):
       html = f"<html><body>Invalid input.</body></html>"

   return HttpResponse(html)

class PostSearch(ListView):
    model = Post
    template_name = 'NewsSearch.html'
    context_object_name = 'Post'
    paginate_by = 10

    def get_queryset(self):

        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset

        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('new.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('new.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('new.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = f'/news/'


