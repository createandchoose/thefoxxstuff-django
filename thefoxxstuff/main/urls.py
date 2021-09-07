from django.urls import path
from .import views
from django.conf import settings

urlpatterns = [
    path('', views.PostList.as_view(), name="stuff"),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
]