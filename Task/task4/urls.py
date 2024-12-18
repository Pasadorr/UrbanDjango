from django.urls import path
from .views import home, platform, cart, games

urlpatterns = [
    path('', home, name='home'),                       # Основной маршрут
    path('platform/', platform, name='platform'),     # Для платформы
    path('cart/', cart, name='cart'),                 # Для корзины
    path('games/', games, name='games'),               # Для игр
]