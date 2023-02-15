from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register', views.UserRegisterView.as_view(), name='user_register'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         views.activate, name='activate'),
]
