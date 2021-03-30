from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

CUSTOM_USER_FIELDS = (
    'full_name',
    'gender',
    'class_rank',
    'major',
    'picture',
    'description',
    'roommates',
    'semesters',
    'bedtime',
    'politics',
    'tidiness_factor',
    'party_factor',
    'guest_factor',
)


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = CUSTOM_USER_FIELDS


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = CUSTOM_USER_FIELDS
