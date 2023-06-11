from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('Signup/', views.signup_view, name='Signup'),
    path('Signin/', views.signin_view, name='Signin'),
    path('Logout/', views.logout_view, name='Logout'),
    path('Auction/', views.auction_view, name='Auction'),
    path('Lienhe/', views.lienhe_view, name='Lienhe'),
    path('Goods/<str:pk>', views.goods_view, name='Goods'),
    path('Search/', views.search_view, name='Search'),
    path('Search/<str:types>/', views.searchtype_view, name='Searchtypes'),
    path('User/', views.user_view, name='User'),
    path('Changeyourpassword/', views.changepw_view, name='Changeyourpassword'),
    path('Information/', views.Information_view, name='Information'),

]
