from django.shortcuts import get_object_or_404, render
from .models import Blog


# Create your views here.
def all_blogs(request):
    Blogs = Blog.objects.order_by("-date")  # -date is for descending order
    return render(request, "blog/all_blogs.html", {"blogs": Blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # pk is primary key
    return render(request, "blog/detail.html", {"blog": blog})
