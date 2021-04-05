from django.test import TestCase
from users.models import Profile


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

    def test_default_value_tidinessFactor(self):
        profile1 = Profile()
        assert profile1.tidiness_factor == 3

    def test_change_value_tidinessFactor(self):
        profile2 = Profile()
        profile2.tidiness_factor = 1
        assert profile2.tidiness_factor == 1

    def test_default_value_partyFactor(self):
        profile1 = Profile()
        assert profile1.party_factor == 3

    def test_change_value_partyFactor(self):
        profile2 = Profile()
        profile2.party_factor = 2
        assert profile2.party_factor == 2

    def test_default_value_guestFactor(self):
        profile1 = Profile()
        assert profile1.guest_factor == 3

    def test_change_value_guestFactor(self):
        profile2 = Profile()
        profile2.guest_factor = 3
        assert profile2.guest_factor == 3
