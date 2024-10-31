from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name = 'home'),
  path('market/', views.market, name = 'market'),
  path('cart/', views.cart, name = 'cart'),
  path('about/', views.about, name = 'about'),
  path('login/', views.login, name = 'login'),
  path('signup/', views.signup, name = 'signup'),
]