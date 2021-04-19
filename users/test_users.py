from django.test import TestCase
from users.models import Profile, create_user_profile, save_user_profile
from users.forms import UserForm,ProfileForm,RegisterForm
from django.forms import ModelForm
from django.contrib.auth.models import User
import datetime

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
        assert profile1.major == ""

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

    def test_default_values_bedtime(self):
        profile1 = Profile()
        assert profile1.bedtime == datetime.time(0, 0, 0)

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
        assert form.Meta.fields == ('gender','class_rank','major',
                                    'picture','description','roommates',
                                    'semesters','bedtime','politics',
                                    'tidiness_factor','party_factor',
                                    'guest_factor', 'min_match_percentage')

    def test_default_model_ProfileForm(self):
        form = ProfileForm(ModelForm)
        assert form.Meta.model == Profile

    def test_default_fields_RegisterForm(self):
        form = RegisterForm(ModelForm)
        assert form.Meta.fields == ('gender','class_rank','major',
                                    'picture','description','roommates',
                                    'semesters','bedtime','politics',
                                    'tidiness_factor','party_factor',
                                    'guest_factor', 'min_match_percentage')

    def test_default_model_RegisterForm(self):
        form = RegisterForm(ModelForm)
        assert form.Meta.model == Profile

    # will later make picture test for blank picture once that is working

    # userConfig tests from users.apps did not seem possible

    # testing views did not seem possible directly. Would likely need to test manualy.

    # testing admin, can test fieldsets, was not sure what they were.

    # testing forms does not seem possible with the except of fields

    # could not figure out a way to test get_photo_url from models or create_user_profile from models
