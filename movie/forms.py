
from django import forms
from django.contrib.auth.models import User
from .models import userprofile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required= True)

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required= True)

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userprofile
        fields = ['phone_number', 'profile_photo', 'bio']
