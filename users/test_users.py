from django.test import TestCase
from users.models import CustomUser
# Create your tests here.


class CustomUserTestCase(TestCase):

    def test_defaultValuesPolitics(self):
        user1 = CustomUser()
        assert user1.politics == "U"

    def test_changeValuePolitics(self):
        user2 = CustomUser()
        user2.politics = "C"
        assert user2.politics == "C"

    def test_defaultValuesFullName(self):
        user1 = CustomUser()
        assert user1.full_name == ""

    def test_changeValueFullName(self):
        user2 = CustomUser()
        user2.full_name = "test name"
        assert user2.full_name == "test name"

    def test_defaultValuesGender(self):
        user1 = CustomUser()
        assert user1.gender == "U"

    def test_changeValueGender(self):
        user2 = CustomUser()
        user2.gender = "F"
        assert user2.gender == "F"

    def test_defaultValuesClassRank(self):
        user1 = CustomUser()
        assert user1.class_rank == "U"

    def test_changeValueClassRank(self):
        user2 = CustomUser()
        user2.class_rank = 2
        assert user2.class_rank == 2

    def test_defaultValuesMajor(self):
        user1 = CustomUser()
        assert user1.major == ""

    def test_changeValueMajor(self):
        user2 = CustomUser()
        user2.major = "Computer Science"
        assert user2.major == "Computer Science"

    def test_defaultValuesDescription(self):
        user1 = CustomUser()
        assert user1.description == ""

    def test_changeValueDescription(self):
        user2 = CustomUser()
        user2.description = "test description"
        assert user2.description == "test description"

    def test_defaultValuesTidinessFactor(self):
        user1 = CustomUser()
        assert user1.tidiness_factor == 3

    def test_changeValueTidinessFactor(self):
        user2 = CustomUser()
        user2.tidiness_factor = 1
        assert user2.tidiness_factor == 1

    def test_defaultValuesPartyFactor(self):
        user1 = CustomUser()
        assert user1.party_factor == 3

    def test_changeValuePartyFactor(self):
        user2 = CustomUser()
        user2.party_factor = 2
        assert user2.party_factor == 2

    def test_defaultValuesGuestFactor(self):
        user1 = CustomUser()
        assert user1.guest_factor == 3

    def test_changeValueGuestFactor(self):
        user2 = CustomUser()
        user2.guest_factor = 3
        assert user2.guest_factor == 3

    def test_defaultValuesSleepLateFactor(self):
        user1 = CustomUser()
        assert user1.sleep_late_factor == 3

    def test_changeValueSleepLateFactor(self):
        user2 = CustomUser()
        user2.sleep_late_factor = 5
        assert user2.sleep_late_factor == 5