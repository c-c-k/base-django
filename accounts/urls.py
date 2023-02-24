import django.contrib.auth.urls
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from . import views

app_name = 'accounts'
urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', include(django.contrib.auth.urls)),
    path('', RedirectView.as_view(url=reverse_lazy('accounts:profile'))),
]