from django.urls import path
from .views import post_list, post_detail, post_new, post_edit, post_delete

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/new/', post_new, name='post_new'),
    path('posts/<int:pk>/edit/', post_edit, name='post_edit'),
    path('posts/<int:pk>/delete/', post_delete, name='post_delete'),
]
