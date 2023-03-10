from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email","is_staff", "is_project_manager", "is_owner")

    def save(self, commit=True):
        user = super(CustomUser, self).save(commit=True)
        if commit:
            user.save()

        # Add stuff like 
        # user.email =self.cleaned_data[\email]     
        return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email", "is_staff", "is_project_manager", "is_owner",)
