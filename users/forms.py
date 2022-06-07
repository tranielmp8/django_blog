from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(
        help_text='A valid email address please', required=False)
    password1 = forms.CharField(
        label='Enter Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    # Meta class is what fields we want to use and to show  from the User Creation/Registration Form
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        help_texts = {
            'username': None
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    # Meta class is what fields we want to use and to show  from the User Creation/Registration Form

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email']
        help_texts = {
            'username': None
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False


class ProfilePictureForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False, label="Change Profile Pic")

    class Meta:
        model = Profile
        fields = ['profile_pic']
