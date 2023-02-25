# https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.views

from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from ..forms import UserCreationForm


class GenericProfileView(View):
    template_name = 'accounts/profile.html'
    unauthenticated_url = reverse_lazy('accounts:login')

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect(self.unauthenticated_url)


class GenericRegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:user_menu')
    template_name = 'registration/register.html'


class GenericLoginView(auth_views.LoginView):
    pass


class GenericLogoutView(auth_views.LogoutView):
    pass


class GenericPasswordChangeView(auth_views.PasswordChangeView):
    pass


class GenericPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    pass


class GenericPasswordResetView(auth_views.PasswordResetView):
    pass


class GenericPasswordResetDoneView(auth_views.PasswordResetDoneView):
    pass


class GenericPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    pass


class GenericPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    pass
