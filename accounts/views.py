from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, UserCreationForm
from .models import OtpCode, User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect


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
            User.objects.create_user(cd['first_name'], cd['last_name'], cd['email'], cd['password1'])
            messages.success(request, 'you registered successfully', 'success')
            return redirect('landing:landing')
        return render(request, self.template_name, {'form': form})

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
