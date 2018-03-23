from django.urls import path

from .views import (
    accounts_signup,
    accounts_login,
    accounts_logout
)

app_name = 'accounts_app'
urlpatterns = [
    path('accounts/signup/', accounts_signup, name='signup'),
    path('accounts/login/', accounts_login, name='login'),
    path('accounts/logout/', accounts_logout, name='logout')
]