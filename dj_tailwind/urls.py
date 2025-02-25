from django.urls import path
from . import views


app_name = 'dj_tailwind'

urlpatterns = [
    path('', views.index, name='dashboard'),
]
