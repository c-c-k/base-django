from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from ..forms import UserCreationForm


class CustomRegisterView(View):
    form = UserCreationForm

    def get(self, request):
        context = {'form': self.form}
        return render(request, 'registration/register.html', context=context)

    def post(self, request):
        form = self.form(request)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
        else:
            context = {'form': form.cleaned_data}
            return render(request, 'registration/register.html',
                          context=context)
