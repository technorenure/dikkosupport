from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.Login, name='login'),
    path('registeration', views.registeration, name='registeration'),
    path('success', views.success, name='success'),
    path('logout', views.Logout, name='logout'),
]