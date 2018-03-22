from django import forms

from .models import Contact_Us

class SendInquiryForm(forms.ModelForm):
    cust_name = forms.CharField(label="Name")
    cust_email_address = forms.EmailField(label="Email Address", help_text='example@yahoo.com')
    cust_contact_number = forms.CharField(label="Contact Number", widget=forms.NumberInput, max_length=12, help_text='Example: 639191234567')
    cust_location = forms.CharField(label="Installation Location", max_length=250, widget=forms.Textarea(attrs={'cols': 10, 'rows': 5}))
    cust_inquiry = forms.CharField(label="Inquiry", max_length=1000, widget=forms.Textarea(attrs={'cols': 10, 'rows': 5}))

    class Meta:
        model = Contact_Us
        fields = ['cust_name', 'cust_email_address', 'cust_contact_number', 'cust_location', 'cust_inquiry']

class MarkAsReadForm(forms.ModelForm):

    class Meta:
        model = Contact_Us
        fields = ('id', 'marked_read')

#==========================version ko=================================

# class MarkAsReadForm(forms.ModelForm):
#     pk = forms.IntegerField(widget=forms.HiddenInput)
#     marked_read = forms.BooleanField(widget=forms.HiddenInput)
#
#     class Meta:
#         model = Contact_Us
#         fields = []


#===========================from facebook================================

# class MarkAsReadForm(forms.ModelForm):
#     class Meta:
#         model = Contact_Us
#         fields = ['id']


# def __init__(self, ticket, *args, **kwargs):
#     super(MarkAsReadForm, self).__init__(*args, **kwargs)
#     self.fields['id'].widget = forms.HiddenInput()