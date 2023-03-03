from django.shortcuts import render, redirect
from django.views import View

from order.models import Order
from .forms import UserRegistrationForm, UserCreationForm, UserLoginForm, EditUserForm
from .models import User, Address
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'register.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('landing:landing')
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['email'], cd['first_name'], cd['last_name'], cd['password1'])
            messages.success(request, 'Registered successfully', 'success')
            return redirect('landing:landing')
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'main_login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print('OK post')
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully', 'success')
                return redirect(request.META.get('HTTP_REFERER'))
            messages.error(request, 'Password is incorrect', 'warning')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully', 'success')
        return redirect('landing:landing')


class UserProfileView(LoginRequiredMixin, View):
    form_class = EditUserForm
    template_name = 'profile.html'

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        form = self.form_class(instance=request.user)
        addresses = Address.objects.filter(user_id=user_id)
        print(addresses)
        orders = Order.objects.filter(user_id=user_id)
        print(orders)
        return render(request, self.template_name, {'user': user, 'form': form, 'addresses':addresses, 'orders':orders})


# class UserRegisterVerifyCodeView(View):
#     form_class = VerifyCodeForm
#     template_name = 'verify.html'
#
#     def get(self, request):
#         form = self.form_class
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         pass


# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         # return redirect('home')
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')
class UserEditView(LoginRequiredMixin, View):
    form_class = EditUserForm
    template_name = 'profile.html'

    # def get(self, request):
    #     form = self.form_class
    #     print('hi', {form})
    #     return render(request, self.template_name, {'form': form})

    def post(self, request):
        pass
