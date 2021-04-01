from django.shortcuts import render

# Create your views here.

def Blog(request):
    return render(request,'blog/blog_page.html')