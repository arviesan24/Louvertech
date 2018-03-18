from django.db import models
from django.urls import reverse

# Create your models here.
class Contact_Us(models.Model):
    cust_name = models.CharField(max_length=120)
    cust_email_address = models.EmailField()
    cust_contact_number = models.IntegerField(blank=True)
    cust_location = models.CharField(max_length=250)
    cust_inquiry = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    marked_read = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("contact_us_app:contact_us")

    def get_message_details_url(self):
        return reverse("contact_us_app:inquiry_details")
