from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.http import HttpResponse

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
    return HttpResponse(f'mostrando post {id}...')

# http://127.0.0.1/edit/<id>/
def post_edit(request, id):
    ...

# http://127.0.0.1/delete/<id>/
def post_delete(request, id):
    ...


def add(request, x, y):
    variaveis = {"answer": int(x) + int(y)}
    return render(request, 'blog/add.html', variaveis)