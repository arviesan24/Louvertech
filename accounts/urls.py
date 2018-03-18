from django.urls import path

from .views import (
    accounts_signup,
    accounts_login,
)

app_name = 'gallery_app'
urlpatterns = [
    path('accounts/signup', accounts_signup, name='signup'),
    path('accounts/login/', accounts_login, name='login')
]