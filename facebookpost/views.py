from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

from .models import Share
from django.urls import reverse_lazy

class HomePageView(ListView):
    template_name ='home.html'
    model = Share

class PostDetailsView(DetailView):
    template_name = 'details.html'
    model=Share    

class PostCreateView(CreateView):
    template_name = 'add.html'
    model=Share    
    fields = ['title', 'author', 'body']    
class PostUpdateView(UpdateView):
    template_name = 'update.html'
    model=Share    
    fields = ['title', 'author', 'body']    
class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    model=Share    
    fields = ['title', 'author', 'body']  
    success_url = reverse_lazy('home')    

