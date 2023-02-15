from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, UserCreationForm, VerifyCodeForm
import random
# from utils import send_otp_code
from .models import OtpCode, User
from django.contrib import messages


# Create your views here.

class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # random_code = random.randint(100000, 999999)
            #  send_otp_code(form.cleaned_data['email'], random_code)
            # OtpCode.objects.create(email=form.cleaned_data['email'], code=random_code)
            # request.session['user_registration_info'] = {
            #     'email': form.cleaned_data['email'],
            #     'first_name': form.cleaned_data['first_name'],
            #     'last_name': form.cleaned_data['last_name'],
            #     'password': form.cleaned_data['password1']
            # }
            # messages.success(request, 'Verification code has been sent to your email', 'success')
            cd = form.cleaned_data
            User.objects.create_user(cd['email'], cd['first_name'], cd['last_name'], cd['password1'])
            messages.success(request, 'you are registered', 'success')
            return redirect('products:landing')
        return render(request, self.template_name, {'form': form})


class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm
    template_name = 'verify.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        pass
