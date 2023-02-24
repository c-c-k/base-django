import django.contrib.auth.urls
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from . import views

app_name = 'accounts'
urlpatterns = [
    # Local views
    # -----------
    path('', RedirectView.as_view(url=reverse_lazy('accounts:profile'))),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),

    # Django builtin authentication views overrides
    # :note: While it's possible to import the views directly from
    #        django.contrib.auth.views and pass in parameters to the
    #        as_view() method call, subclassing and modifying them via
    #        local views feels like a more organized approach.
    # https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.views

    # path("login/", views.LoginView.as_view(), name="login"),
    # path("logout/", views.LogoutView.as_view(), name="logout"),
    # path("password_change/", views.PasswordChangeView.as_view(),
    #      name="password_change"),
    # path("password_change/done/", views.PasswordChangeDoneView.as_view(),
    #      name="password_change_done",),
    # path("password_reset/", views.PasswordResetView.as_view(),
    #      name="password_reset"),
    # path("password_reset/done/", views.PasswordResetDoneView.as_view(),
    #      name="password_reset_done",),
    # path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(),
    #      name="password_reset_confirm",),
    # path("reset/done/", views.PasswordResetCompleteView.as_view(),
    #      name="password_reset_complete",),

    # Django builtin authentication urls.
    # :important: This must come after the overrides
    #             for the overrides to ta take effect.
    path('', include(django.contrib.auth.urls)),
]