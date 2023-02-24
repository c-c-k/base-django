from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import ExtendedUserCreationForm


class UserMenuView(View):
    def get(self, request):
        return render(request, 'default/profile.html')


class RegisterView(CreateView):
    form_class = ExtendedUserCreationForm
    success_url = reverse_lazy('default:user_menu')
    template_name = 'default/register.html'

# class RegisterView(View)
#     form = UserCreationFormWithPersonalInfo
#
#     def get(self, request):
#         context = {'form': self.form}
#         return render(request, 'accounts/register.html', context=context)
#
#     def post(self, request):
#         form = self.form(request)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('accounts:index'))
#         else:
#             context= {'form': form.cleaned_data}
#             return render(request, 'accounts/register.html', context=context)
