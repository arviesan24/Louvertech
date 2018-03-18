from django.contrib import admin

# Register your models here.
from .models import Contact_Us

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["cust_name", "cust_email_address", "cust_contact_number", "cust_location", "cust_inquiry", "timestamp"]
    list_filter = ["cust_name", "cust_email_address", "marked_read", "timestamp"]
    search_fields = ["cust_name", "cust_email_address", "cust_contact_number", "timestamp"]

    class Meta:
        model = Contact_Us

admin.site.register(Contact_Us, ContactUsAdmin)