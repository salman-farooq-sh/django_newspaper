from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'email', 'age', 'is_staff']

    add_form = CustomUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Personal Information', {'fields': ('age',)}),
    )

    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        ('Personal Information', {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
