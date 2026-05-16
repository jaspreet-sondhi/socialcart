from . import views
from django.urls import path

urlpatterns = [
    path('', views.shops_list, name='shops_list'),
    path('create/', views.shop_create, name='shop_create'),
    path('<int:shop_id>/edit/', views.shop_edit, name='shop_edit'),
    path('<int:shop_id>/delete/', views.shop_delete, name='shop_delete'),
    path('register/', views.register, name='register'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path( '<int:shop_id>/like/', views.like_shop, name='like_shop'),
    path('categories/', views.categories, name='categories'),
    path(
    '<int:shop_id>/favorite/',
    views.favorite_shop,
    name='favorite_shop'
),
path(
    'favorites/',
    views.favorites_list,
    name='favorites_list'
),
] 
