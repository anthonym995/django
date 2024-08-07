from django.urls import path
from . import views

urlpatterns = [
    path('chat', views.chat, name='chat'),
    path('chat/<str:room>/', views.room, name='room'),
    path('send/', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('getDetails/<str:room>/', views.get_details, name='get_details'),
]
