from django.urls import path

from .views import (
    index,
    upload_product,
    product_details
)

app_name = 'gallery'
urlpatterns = [
    path('', index, name='index'),
    path('add_product/', upload_product, name='upload_product'),
    path('gallery/<slug:slug>/', product_details, name='details')
]