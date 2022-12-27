from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path(route='room_page/<str:pk>/', view=views.room, name='room'), 
]
