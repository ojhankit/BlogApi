from django.urls import path
from . import views 

urlpatterns = [
    path('' ,views.blog_list ,name='blog_list'),
    path('<int:blog_id>/',views.blog_detail ,name='blog_detail'),
    path('user_blog/<int:pk>',views.blog_list_user ,name='user_blog'),
    path('create/' ,views.create_blog ,name='create'),
    path('delete/<int:pk>' ,views.delete_blog ,name='delete'),
    path('<int:blog_id>/add_comment/' ,views.add_comment ,name='add_comment'),
]
