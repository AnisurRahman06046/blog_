from django.urls import path
from . import views
urlpatterns = [
    path('add-author/',views.addAuthor,name='addAuthor'),
]