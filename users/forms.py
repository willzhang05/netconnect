from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Profile

CUSTOM_USER_FIELDS = (
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


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = CUSTOM_USER_FIELDS
        labels = {
            # 'gender': 'test',
            # 'class_rank': 'test',
            # 'major': 'test',
            # 'picture': 'test',
            # 'description': 'test',
            # 'roommates': 'test',
            'politics': 'What political views do you most identify with?',
        }
