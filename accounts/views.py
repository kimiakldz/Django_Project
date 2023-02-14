from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm


# Create your views here.

class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        return render(request, 'home.html')
