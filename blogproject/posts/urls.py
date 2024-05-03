from django.urls import path
from . import views
urlpatterns = [
    path('all-posts/', views.posts,name="posts"),
]