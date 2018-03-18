from django.contrib import admin

# Register your models here.
from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "image_location", "timestamp"]
    list_filter = ["name", "description"]
    search_fields = ["name", "description"]

    class Meta:
        model = Gallery

admin.site.register(Gallery, GalleryAdmin)