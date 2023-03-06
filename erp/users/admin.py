from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active", "is_project_manager", "is_owner")
    list_filter = ("email", "is_staff", "is_active", "is_project_manager", "is_owner")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_project_manager", "is_owner", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions","is_staff", "is_project_manager", "is_owner"
            )}
        ),
    )
    search_fields = ("email","is_staff", "is_project_manager", "is_owner")
    ordering = ("email","is_staff", "is_project_manager", "is_owner")


admin.site.register(CustomUser, CustomUserAdmin)