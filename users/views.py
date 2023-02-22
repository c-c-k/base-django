from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import ExtendedUserCreationForm


class IndexView(View):
    def get(self, request):
        return render(request, 'users/index.html')


class RegisterView(CreateView):
    form_class = ExtendedUserCreationForm
    success_url = reverse_lazy('users:index')
    template_name = 'users/register.html'

# class RegisterView(View)
#     form = UserCreationFormWithPersonalInfo
#
#     def get(self, request):
#         context = {'form': self.form}
#         return render(request, 'users/register.html', context=context)
#
#     def post(self, request):
#         form = self.form(request)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('users:index'))
#         else:
#             context= {'form': form.cleaned_data}
#             return render(request, 'users/register.html', context=context)
