from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from client import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('verifylogin/', views.verifylogin, name='verifylogin'),
    path('logout/', views.userlogout, name='userlogout'),
    path('register/', views.register, name='register'),
    path('saveuser/', views.saveuser, name='saveuser'),
    path('food/', views.food, name='food'),
    path('contact/', views.contact, name='contact'),
    # all admin control urls from here
    path('addfood/', views.addFood, name='addfood'),
    path('savefood/', views.savefood, name='savefood'),
    path('orders/', views.orders, name='orders'),
    path('foodlist/', views.foodlist, name='foodlist'),
    path('checkout/', views.checkout, name='checkout'),
    path('users/', views.users, name='users'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)