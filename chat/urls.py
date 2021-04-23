from django.urls import path

from . import views

urlpatterns = [
    path('chat/<str:user_one>-<str:user_two>/', views.room, name='chat_room'),
]
