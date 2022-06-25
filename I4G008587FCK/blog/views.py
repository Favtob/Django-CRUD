from multiprocessing.context import _default_context
from symtable import Class
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import DetailView
from posts.models import post


# Create your views here.
class PostListView(ListView):
    model = Post


class PostCreateViews(CreateView):
    model = Post
    fields = “__all__”
    success_url = reverse_lazy(“blog:all”)


class PostUpdateView(UpdateView):
    model = Post
    fields = “__all__”
    success_url = reverse_lazy(“blog: all”)

class PostDeleteView(DeleteView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostDetailView(DetailView):
    model = Post


 
