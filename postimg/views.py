#from django.shortcuts import render

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Postimg

# Create your views here.

class HomePageView(ListView):
    model = Postimg
    template_name = 'home.html'

class CreatePostView(CreateView):
    model = Postimg
    form_class = PostForm
    template_name = 'postaimage.html'
    success_url = reverse_lazy('home')
