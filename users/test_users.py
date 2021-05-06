from django.test import TestCase
from users.models import *
from users.forms import UserForm, ProfileForm, RegisterForm
from django.forms import ModelForm
from django.contrib.auth.models import User
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from users.matching import matching
from users.models import Profile
from users.apps import UsersConfig
from django.db import models


class ProfileSeleniumTestCase(TestCase):
    pass


class ProfileTestCase(TestCase):

    def test_default_value_politics(self):
        profile1 = Profile()
        assert profile1.politics == 'U'

    def test_change_value_politics(self):
        profile2 = Profile()
        profile2.politics = 'C'
        assert profile2.politics == 'C'

    def test_default_value_gender(self):
        profile1 = Profile()
        assert profile1.gender == 'U'

    def test_change_value_gender(self):
        profile2 = Profile()
        profile2.gender = 'F'
        assert profile2.gender == 'F'

    def test_default_value_class_rank(self):
        profile1 = Profile()
        assert profile1.class_rank == 'U'

    def test_change_value_class_rank(self):
        profile2 = Profile()
        profile2.class_rank = 2
        assert profile2.class_rank == 2

    def test_default_value_major(self):
        profile1 = Profile()
        assert profile1.major == "UNKNOWN"

    def test_change_value_major(self):
        profile2 = Profile()
        profile2.major = "Computer Science"
        assert profile2.major == "Computer Science"

    def test_default_value_description(self):
        profile1 = Profile()
        assert profile1.description == ""

    def test_change_value_description(self):
        profile2 = Profile()
        profile2.description = "test description"
        assert profile2.description == "test description"

    def test_default_value_social_factor(self):
        profile1 = Profile()
        assert profile1.social_factor == 3

    def test_change_value_social_factor(self):
        profile2 = Profile()
        profile2.social_factor = 1
        assert profile2.social_factor == 1

    def test_default_value_tidiness_factor(self):
        profile1 = Profile()
        assert profile1.tidiness_factor == 3

    def test_change_value_tidiness_factor(self):
        profile2 = Profile()
        profile2.tidiness_factor = 1
        assert profile2.tidiness_factor == 1

    def test_default_value_party_factor(self):
        profile1 = Profile()
        assert profile1.party_factor == 3

    def test_change_value_party_factor(self):
        profile2 = Profile()
        profile2.party_factor = 2
        assert profile2.party_factor == 2

    def test_default_value_guest_factor(self):
        profile1 = Profile()
        assert profile1.guest_factor == 3

    def test_change_value_guest_factor(self):
        profile2 = Profile()
        profile2.guest_factor = 3
        assert profile2.guest_factor == 3

    def test_default_value_roommates(self):
        profile1 = Profile()
        assert profile1.roommates == 1

    def test_change_value_roommates(self):
        profile2 = Profile()
        profile2.roommates = 4
        assert profile2.roommates == 4

    def test_default_values_semesters(self):
        profile1 = Profile()
        assert profile1.semesters == 2

    def test_change_value_semesters(self):
        profile2 = Profile()
        profile2.semesters = 5
        assert profile2.semesters == 5

    def test_change_value_bedtime(self):
        profile2 = Profile()
        profile2.bedtime = datetime.time(5, 4, 11)
        assert profile2.bedtime == datetime.time(5, 4, 11)

    def test_default_fields_UserForm(self):
        form1 = UserForm(ModelForm)
        assert form1.Meta.fields == ('first_name', 'last_name', 'email')

    def test_default_model_UserForm(self):
        form = UserForm(ModelForm)
        assert form.Meta.model == User

    def test_change_model_UserForm(self):
        form = UserForm(ModelForm)
        user1 = User
        user1.username = "test"
        form.Meta.model = user1
        assert form.Meta.model.username == "test"

    def test_default_fields_ProfileForm(self):
        form = ProfileForm(ModelForm)
        assert form.Meta.fields == (
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
            'match_enabled',
            'search_lat',
            'search_lng',
            'search_radius')

    def test_default_model_ProfileForm(self):
        form = ProfileForm(ModelForm)
        assert form.Meta.model == Profile

    def test_default_fields_RegisterForm(self):
        form = RegisterForm(ModelForm)
        assert form.Meta.fields == (
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
            'min_match_percentage')

    def test_default_model_RegisterForm(self):
        form = RegisterForm(ModelForm)
        assert form.Meta.model == Profile

    def test_default_value_match_enabled(self):
        profile1 = Profile()
        assert profile1.match_enabled == False

    def test_change_value_match_enabled(self):
        profile1 = Profile()
        profile1.match_enabled = True
        assert profile1.match_enabled

    def test_default_value_min_match_percentage(self):
        profile1 = Profile()
        assert profile1.min_match_percentage == 75

    def test_default_search_lat(self):
        profile1 = Profile()
        assert profile1.search_lat is None

    def test_change_search_lat(self):
        profile1 = Profile()
        profile1.search_lat = 5.0
        assert profile1.search_lat == 5.0

    def test_default_search_lng(self):
        profile1 = Profile()
        assert profile1.search_lng is None

    def test_change_search_lng(self):
        profile1 = Profile()
        profile1.search_lng = 5.0
        assert profile1.search_lng == 5.0

    def test_default_search_radius(self):
        profile1 = Profile()
        assert profile1.search_radius == 1.0

    def test_change_search_radius(self):
        profile1 = Profile()
        profile1.search_radius = 5.0
        assert profile1.search_radius == 5.0

    def test_change_first_name(self):
        form1 = User()
        form1.first_name = "John"
        assert form1.first_name == "John"

    def test_change_last_name(self):
        form1 = User()
        form1.last_name = "Doe"
        assert form1.last_name == "Doe"

    def test_change_email(self):
        form1 = User()
        form1.email = "johndoe@gmail.com"
        assert form1.email == "johndoe@gmail.com"

    def test_matching_default(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-0=100
        profile1 = Profile()
        profile2 = Profile()
        assert matching(profile1, profile2) == 90

    def test_location(self):
        profile1 = Profile()
        profile2 = Profile()

        profile1.search_lat = 1
        profile1.search_lng = 1
        profile1.search_radius = 1
        profile2.search_lat = 1
        profile2.search_lng = 1
        profile2.search_radius = 1

        assert matching(profile1, profile2) == 100

    def test_location_different(self):
        profile1 = Profile()
        profile2 = Profile()

        profile1.search_lat = 2
        profile1.search_lng = 1
        profile1.search_radius = 5
        profile2.search_lat = 1
        profile2.search_lng = 1
        profile2.search_radius = 5

        assert matching(profile1, profile2) == 100

    def test_matching_1_off_roomate(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(10*.5)=85
        profile1 = Profile()
        profile1.roommates = 1
        profile2 = Profile()
        profile2.roommates = 2
        assert matching(profile1, profile2) == (85 / 100) * 100

    def test_matching_3_off_roomate(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(10*1)=80
        profile1 = Profile()
        profile1.roommates = 1
        profile2 = Profile()
        profile2.roommates = 4
        assert matching(profile1, profile2) == (80 / 100) * 100

    def test_matching_1_off_semesters(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(10*.5)=85
        profile1 = Profile()
        profile1.semesters = 1
        profile2 = Profile()
        profile2.semesters = 2
        assert matching(profile1, profile2) == (85 / 100) * 100

    def test_matching_3_off_semesters(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(10*1)=80
        profile1 = Profile()
        profile1.semesters = 1
        profile2 = Profile()
        profile2.semesters = 4
        assert matching(profile1, profile2) == (80 / 100) * 100

    def test_matching_2_off_roomates_and_1_semesters(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(10*.5)-(10*.5)=80
        profile1 = Profile()
        profile1.semesters = 1
        profile1.roommates = 1
        profile2 = Profile()
        profile2.semesters = 3
        profile2.roommates = 3
        assert matching(profile1, profile2) == (80 / 100) * 100

    def test_matching_2_off_roomates_and_3_semesters(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(10*.5)-(10*1)=75
        profile1 = Profile()
        profile1.semesters = 1
        profile1.roommates = 1
        profile2 = Profile()
        profile2.semesters = 4
        profile2.roommates = 3
        assert matching(profile1, profile2) == (75 / 100) * 100

    def test_wrong_class_rank(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(10*1)=80
        profile1 = Profile()
        profile1.class_rank = 1
        profile2 = Profile()
        profile2.class_rank = 2
        assert matching(profile1, profile2) == (80 / 100) * 100

    def test_wrong_major(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(5*1)=80
        profile1 = Profile()
        profile1.major = "CS"
        profile2 = Profile()
        profile2.major = "Arch"
        assert matching(profile1, profile2) == (85 / 100) * 100

    def test_wrong_politics(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(5*1)=80
        profile1 = Profile()
        profile1.politics = "Moderate"
        profile2 = Profile()
        profile2.politics = "Conservative"
        assert matching(profile1, profile2) == (85 / 100) * 100

    def test_social_factor_1_off(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(20-20*(4-|2-1|)/4)=100-(20-20*3/4) = 85
        profile1 = Profile()
        profile1.social_factor = 1.0

        profile2 = Profile()
        profile2.social_factor = 2.0
        assert matching(profile1, profile2) == (85.0 / 100) * 100.0

    def test_social_factor_3_off(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(20-20*(4-|4-1|)/4)=100-(20-20*1/4) = 75
        profile1 = Profile()
        profile1.social_factor = 1.0

        profile2 = Profile()
        profile2.social_factor = 4.0
        assert matching(profile1, profile2) == (75.0 / 100) * 100.0

    def test_tidiness_factor_1_off(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(15-15*(4-|2-1|)/4)=100-(15-15*3/4)
        profile1 = Profile()
        profile1.tidiness_factor = 1.0

        profile2 = Profile()
        profile2.tidiness_factor = 2.0
        assert matching(profile1, profile2) == (
            (100.0 - (10.0 + 15.0 - 15.0 * 3.0 / 4.0)) / 100) * 100.0

    def test_tidiness_factor_4_off(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(15-15*(4-|5-1|)/4)=100-(15-0) = 75
        profile1 = Profile()
        profile1.tidiness_factor = 1.0

        profile2 = Profile()
        profile2.tidiness_factor = 5.0
        assert matching(profile1, profile2) == (75 / 100) * 100.0

    def test_party_factor_1_off(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(10-10*(4-|2-1|)/4)=100-(10-10*3/4) = 87.5
        profile1 = Profile()
        profile1.party_factor = 1.0

        profile2 = Profile()
        profile2.party_factor = 2.0
        assert matching(profile1, profile2) == (87.5 / 100) * 100.0

    def test_party_factor_2_off(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(10-10*(4-|3-1|)/4)=100-(10-10*2/4) = 85
        profile1 = Profile()
        profile1.party_factor = 1.0

        profile2 = Profile()
        profile2.party_factor = 3.0
        assert matching(profile1, profile2) == (85.0 / 100.0) * 100.0

    def test_guest_factor_1_off(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(5-5*(4-|2-1|)/4)=100-(5-5*3/4)
        profile1 = Profile()
        profile1.guest_factor = 1.0

        profile2 = Profile()
        profile2.guest_factor = 2.0
        assert matching(profile1, profile2) == (
            (100.0 - (10.0 + 5.0 - 5.0 * 3.0 / 4.0)) / 100) * 100.0

    def test_guest_factor_3_off(self):
        # (class_rank (10) + major (5) + roomates (10) + semesters (10) + politics (5) + social_factor (20)
        # tidiness_factor (15) + party_factor (10) + guest_factor (5)) = 100
        # total points/100*100
        # total points = 100-(5-5*(4-|4-1|)/4)=100-(5-5*1/4)
        profile1 = Profile()
        profile1.guest_factor = 1.0

        profile2 = Profile()
        profile2.guest_factor = 4.0
        assert matching(profile1, profile2) == (
            (100.0 - (10.0 + 5.0 - 5.0 * 1.0 / 4.0)) / 100) * 100.0

    def test_user_apps(self):
        assert UsersConfig.name == 'users'

    def test_models_field_gender(self):
        assert GENDER_CHOICES == (
            ('F', 'Female'), ('M', 'Male'), ('O', 'Other'), ('U', 'Prefer not to say'),)

    def test_models_field_class(self):
        assert CLASS_RANK_CHOICES == (
            ('1',
             'First Year'),
            ('2',
             'Second Year'),
            ('3',
             'Third Year'),
            ('4',
             'Fourth Year'),
            ('G',
             'Graduate Student'),
            ('U',
             'Prefer not to say'),
        )

    def test_models_field_political(self):
        assert POLITICAL_VIEW_CHOICES == (
            ('L', 'Liberal'), ('M', 'Moderate'), ('C', 'Conservative'), ('U', 'Prefer not to say'),)

    def test_str_username(self):
        profile1 = Profile()
        user1 = User()
        profile1.user = user1
        profile1.user.username = "johndoe"
        assert str(profile1) == "johndoe"

    def test_photo_url(self):
        profile1 = Profile()
        user1 = User()
        profile1.user = user1
        assert profile1.get_photo_url[37:48] == "default.jpg"
