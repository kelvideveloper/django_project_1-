from django.contrib import admin
from django.urls import path
from coreapp.views import home, login_view, cadastro_view, termos, logout_view

app_name = "coreapp"

urlpatterns = [
    path('', home, name='home'),
    path('login', login_view, name='login'),
    path('cadastro', cadastro_view, name='cadastro'),
    path('termos de uso', termos, name='termos'),
    path('logout', logout_view, name='logout'),
]