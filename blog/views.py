from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

# http://127.0.0.1/
def post_list(request):
    posts = (
        Post.objects
            .filter(published_date__lte=timezone.now())
            .order_by('published_date')
    )
    return render(request, 'blog/post_list.html', {"posts": posts})

# http://127.0.0.1/read/<id>/
def post_read(request, id):
    ...

# http://127.0.0.1/edit/<id>/
def post_edit(request, id):
    ...

# http://127.0.0.1/delete/<id>/
def post_delete(request, id):
    ...