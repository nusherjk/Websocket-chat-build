# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.Landing.as_view(), name="index"),
    path("<str:room_name>/", views.Room.as_view(), name="room"),
    # path("chat/", views.chat, name="chat"),
]