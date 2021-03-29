from users.models import CustomUser


def create_profile(strategy, details, response, user, *args, **kwargs):
    user = CustomUser.objects.filter(username=details['username']).first()
    if not user:
        user = CustomUser(username=details['username'])

    user.full_name = details['fullname']
    user.save()

    return kwargs
