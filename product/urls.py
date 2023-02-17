from django.urls import path
from . import views

app_name = 'landing'
urlpatterns = [
    path('', views.LandingView.as_view(), name='landing'),
    path('shop', views.ShopView.as_view(), name='shop'),
    path('category/<slug:category_slug>/', views.ShopView.as_view(), name='category_filter'),
    path('product/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
