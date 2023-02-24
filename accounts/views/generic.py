from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from ..forms import ExtendedUserCreationForm


class GenericProfileView(View):
    template_name = 'accounts/profile.html'
    unauthenticated_url = reverse_lazy('accounts:login')

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect(self.unauthenticated_url)


class GenericRegisterView(CreateView):
    form_class = ExtendedUserCreationForm
    success_url = reverse_lazy('accounts:user_menu')
    template_name = 'registration/register.html'

