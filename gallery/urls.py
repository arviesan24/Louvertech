from django.urls import path

from .views import (
    index,
    upload_product,
    edit_product,
    product_details,
)

app_name = 'gallery_app'
urlpatterns = [
    path('', index, name='index'),
    path('add_product/', upload_product, name='upload_product'),
    path('edit_product/<slug:slug>/',edit_product, name='edit_product'),
    path('gallery/<slug:slug>/', product_details, name='details')
]