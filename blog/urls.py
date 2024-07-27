from django.urls import path
from . import views 

urlpatterns = [
    path('' ,views.blog_list ,name='blog_list'),
    path('create/' ,views.create_blog ,name='create'),
    path('user_blog/<int:pk>',views.blog_list_user ,name='user_blog'),
    path('delete/<int:pk>' ,views.delete_blog ,name='delete'),
]
