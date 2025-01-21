from django.urls import path
from app import views
urlpatterns = [
    path('', views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),
    path('laptop/',views.laptop,name='laptop'),
    path('laptop/<slug:data>/',views.laptop,name='laptopdata'),
    path('topwears/',views.topwears,name='topwears'),
    path('topwears/<slug:data>/',views.topwears,name='topwearsdata'),
    path('bottomwears/',views.bottomwears,name='bottomwears'),
    path('bottomwears/<slug:data>/',views.bottomwears,name='bottomwearsdata'),
    path('login/', views.login, name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]
