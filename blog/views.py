from django.shortcuts import render


# http://127.0.0.1/
def post_list(request):
    return render(request, 'blog/post_list.html', {"nome": "World"})

# http://127.0.0.1/read/<id>/
def post_read(request, id):
    ...

# http://127.0.0.1/edit/<id>/
def post_edit(request, id):
    ...

# http://127.0.0.1/delete/<id>/
def post_delete(request, id):
    ...