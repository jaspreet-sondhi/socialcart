from django import forms
from .models import Shop
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class shopsForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['text','photo','category']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'profile_image', 'location', 'website']        