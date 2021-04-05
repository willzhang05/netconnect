from django.contrib.auth.models import User
from users.models import Profile


def create_profile(strategy, details, response, user, *args, **kwargs):
    profile = Profile.objects.filter(user=user).first()
    if not profile:
        user = User(**details)
        profile = Profile(user=user)
    user.save()
    profile.save()

    return kwargs
