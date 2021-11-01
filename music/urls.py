from django.urls import path
from . import views

urlpatters = [
    path('music/', views.SongList.as_views()),
]
