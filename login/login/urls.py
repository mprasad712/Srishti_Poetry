from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.login_view, name='signin'),
    path('signup/', views.register, name='signup'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('home/', views.homepage, name='home'),
    path('poems/', views.poems, name='poems'),
]
