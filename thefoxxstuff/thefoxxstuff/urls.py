"""Конфигурация URL-адреса foxxstuff

Список " URL-шаблоны` направляет URL-адреса в представления. Для получения дополнительной информации, пожалуйста, смотрите:
https://docs.djangoproject.com/en/3.2/topics/http/urls/
Примеры:
Представления функций
1. Добавьте импорт: из представлений импорта my_app
2. Добавьте URL-адрес в urlpatterns: path(", views.home, name='home')
Представления на основе классов
1. Добавьте импорт: из other_app.views import Home
2. Добавьте URL-адрес в url-шаблоны: path(", Home.as_view(), name='home')
Включая другой URLconf
1. Импортируйте функцию include (): из django.urls импортируйте include, путь
2. Добавьте URL-адрес в url-шаблоны: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
