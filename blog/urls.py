from django.urls import path
from blog.views import (BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView,CommentDeleteView,CommentCreateView)


app_name='blog'

urlpatterns=[
    
    path('',BlogListView.as_view(),name='list'),
    path('<int:blog_pk>/',BlogDetailView.as_view(),name='detail'),
    path('create/',BlogCreateView.as_view(),name='create'),
    path('<int:pk>/update/',BlogUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',BlogDeleteView.as_view(),name='delete'),
    path('<int:pk>/comment/delete/',CommentDeleteView.as_view(),name='comment_delete'),
    
    path('comment/create/<int:blog_pk>/',CommentCreateView.as_view(),name='comment_create'),
]