from django.urls import path
from . import views

urlpatterns = [
    path('read/<id>/', views.post_read, name='post_list'),
    path('edit/<id>/', views.post_edit, name='post_edit'),
    path('delete/<id>/', views.post_delete, name='post_delete'),
    path('add/<x>/<y>/', views.add, name='add'),
    path('', views.post_list, name='post_list'),
]