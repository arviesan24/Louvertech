from django import forms

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()

class AccountRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label="Email Address", max_length=120)
    email2 = forms.EmailField(label="Confirm Email", max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Reenter Password")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            'password2',
        ]

    def clean_email2(self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email != email2:
            raise forms.ValidationError("Please confirm Email.")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Password doesn't match.")
        return password

class AccountLoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)  # compare user input from DB

            if user is not None:
                return super(AccountLoginForm, self).clean(*args, **kwargs)  # if no errors return user

            else:
                raise forms.ValidationError("Incorrect username or password.")