from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import UserCreationFormWithPersonalInfo


class IndexView(View):
    def get(self, request):
        render(request, 'users/index.html')


class RegisterView(View):
    form = UserCreationFormWithPersonalInfo

    def get(self, request):
        context = {'form': self.form}
        return render(request, 'users/register.html', context=context)

    def post(self, request):
        form = self.form(request)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:index'))
        else:
            context= {'form': form.cleaned_data}
            return render(request, 'users/register.html', context=context)
