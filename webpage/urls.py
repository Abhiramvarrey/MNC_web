from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('register/', views.register_user, name="register"),
    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('home/',views.home,name='home'),
    path('', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
]
