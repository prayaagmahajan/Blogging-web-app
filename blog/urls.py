from django.urls import path
from . import views
from .views import postlisview,postdetailview,postcreateview,postupdateview,postdeleteview,userpostlisview

urlpatterns = [
    path('', postlisview.as_view(),name='blog-home'),
    path('user/<str:username>', userpostlisview.as_view(),name='user-posts'),
    path('about/', views.about,name='blog-about'),
    path('post/<int:pk>/', postdetailview.as_view(),name='post-detail'),
    path('post/new/', postcreateview.as_view(),name='post-create'),
    path('post/<int:pk>/update', postupdateview.as_view(),name='post-update'),
    path('post/<int:pk>/update', postupdateview.as_view(),name='post-update'),
    path('post/<int:pk>/delete', postdeleteview.as_view(),name='post-delete'),



]