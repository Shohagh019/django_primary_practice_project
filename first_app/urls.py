from django.urls import path
from . import views
urlpatterns = [
    path('product/', views.product, name = 'product'),
    path('login/', views.login, name = 'login'),
    path('about/', views.about, name = 'about'),
    path('v-form/', views.djangoForm, name = 'd-form'),
    path('d-form/', views.validatedForm, name = 'v-form'),
    path('p-form/', views.passValidator, name = 'p-form'),
]