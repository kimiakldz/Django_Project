from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('creat', views.OrderCreateView.as_view(), name='Order_creat'),
    path('detail/<int:order_id>', views.OrderDetailView.as_view(), name='Order_detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
    path('applycode/<int:order_id>/', views.CodeApplyView.as_view(), name='code_apply'),
    path('placeorder/<int:order_id>/', views.PlaceOrderView.as_view(), name='place_order'),
]
