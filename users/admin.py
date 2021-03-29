from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .forms import CUSTOM_USER_FIELDS


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': CUSTOM_USER_FIELDS}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
