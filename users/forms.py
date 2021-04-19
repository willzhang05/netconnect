from django.forms import ModelForm, TextInput
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
    'min_match_percentage',
)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [field.name for field in Profile._meta.get_fields()]


class RegisterForm(ModelForm):
    class Meta:
        model = Profile
        fields = CUSTOM_USER_FIELDS
        labels = {
            'class_rank': 'What year in school are you?',
            'major': 'What\'s your major?',
            'picture': 'Upload a profile picture!',
            'description': 'Add any information about yourself you would like potential roommates to see.',
            'roommates': 'How many roommates are you looking for?',
            'semesters': 'For how many semesters are you looking to room?',
            'bedtime': 'Around what time do you usually go to sleep?',
            'politics': 'What political views do you most identify with?',
            'tidiness_factor': 'On a scale from 1-5, how organized/tidy would you consider yourself?',
            'party_factor': 'On a scale from 1-5, how frequently do you go out/party?',
            'guest_factor': 'On a scale from 1-5, how frequently would you like to have guests over?',
            'min_match_percentage': 'What would you like your minimum match percentage to be?',
        }
        widgets = {
            'tidiness_factor': TextInput(attrs={'type': 'range', 'min': 1, 'max': 5}),
            'party_factor':  TextInput(attrs={'type': 'range', 'min': 1, 'max': 5}),
            'guest_factor':  TextInput(attrs={'type': 'range', 'min': 1, 'max': 5}),
            'min_match_percentage':  TextInput(attrs={'type': 'range', 'min': 50, 'max': 100}),
        }
