from django.urls import path
from . import views

app_name = 'vitech'

urlpatterns = [
        path('', views.home, name="home"),
]
