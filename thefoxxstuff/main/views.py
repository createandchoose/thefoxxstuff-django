from django.db import models
from django.shortcuts import render, redirect
from .models import Post
from django.views import generic


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'