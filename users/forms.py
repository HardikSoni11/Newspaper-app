from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',) # meta here -> default && additional age field added
        fields = ('username', 'email', 'age') ## all fields added by overselves **default password field will 
        # still appear so use this way only!!

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        # fields = UserChangeForm.Meta.fields # same as above
        fields = ('username', 'email', 'age')