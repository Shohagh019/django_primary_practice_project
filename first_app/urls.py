from django.urls import path
from . import views
urlpatterns = [
    path('product/', views.product, name = 'product'),
    path('login/', views.login, name = 'login'),
    path('about/', views.about, name = 'about'),
    path('d-form/', views.djangoForm, name = 'd-form'),
]