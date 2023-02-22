from django.urls import path

from . import views

appname = 'users'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
]