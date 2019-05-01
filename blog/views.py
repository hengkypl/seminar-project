from django.shortcuts import render

# Create your views here.
# Create your views here.
def homeblog(request):
    return render(request, 'blog/blog.html')
