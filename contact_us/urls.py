from django.urls import path

from .views import (
    contact_us,
    all_inquiries,
    unread_inquiries,
    read_inquiries,
    inquiry_details,
    mark_as_read,
    delete_inquiries
)

app_name = 'contact_us_app'
urlpatterns = [
    path('contact-us/', contact_us, name='contact_us'),

    path('messages/', all_inquiries, name='all_inquiries'),
    path('messages/unread/', unread_inquiries, name='unread_inquiries'),
    path('messages/read/', read_inquiries, name='read_inquiries'),

    path('messages/<int:pk>/', inquiry_details, name='inquiry_details'),
    path('mark_as_read/', mark_as_read, name='mark_as_read'),

    path('messages/delete/', delete_inquiries, name='delete_inquiries'),
]