from django.forms import ModelForm, NumberInput, HiddenInput
from django.contrib.auth.models import User

from .models import Profile

PROFILE_FIELDS = (
    'gender',
    'class_rank',
    'major',
    'picture',
    'description',
    'roommates',
    'semesters',
    'politics',
    'social_factor',
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
        fields = PROFILE_FIELDS + \
            ('match_enabled', 'search_lat', 'search_lng', 'search_radius')


class RegisterForm(ModelForm):
    class Meta:
        model = Profile
        fields = PROFILE_FIELDS
        labels = {
            'gender': 'What\'s your gender?',
            'class_rank': 'What year in school are you?',
            'major': 'What\'s your major?',
            'picture': 'Upload a profile picture!',
            'description': 'Add any information about yourself you would like potential roommates to see.',
            'roommates': 'How many roommates are you looking for?',
            'semesters': 'For how many semesters are you looking to room?',
            'politics': 'What political views do you most identify with?',
            'social_factor': 'On a scale from 1-5, how frequently would you want to spend time with roommates?',
            'tidiness_factor': 'On a scale from 1-5, how organized/tidy would you consider yourself?',
            'party_factor': 'On a scale from 1-5, how frequently do you go out/party?',
            'guest_factor': 'On a scale from 1-5, how frequently would you like to have guests over?',
            'min_match_percentage': 'What would you like your minimum match percentage to be?',
        }
        widgets = {
            'roommates': NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5}),
            'semesters': NumberInput(attrs={'type': 'range', 'min': 1, 'max': 8}),
            'social_factor': NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5}),
            'social_factor': NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5}),
            'tidiness_factor': NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5}),
            'party_factor':  NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5}),
            'guest_factor':  NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5}),
            'min_match_percentage':  NumberInput(attrs={'type': 'range', 'min': 0, 'max': 100, 'step': 0.1}),
        }
