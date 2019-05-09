from django.shortcuts import render
from .models import Blog

# Create your views here.
# Create your views here.
def homeblog(request):
    zblog = Blog.objects
    return render(request, 'blog/blog.html', {'zblog': zblog})
