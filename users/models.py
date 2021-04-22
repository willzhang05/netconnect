import datetime
from django.db import models
from django.contrib.auth.models import User, AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.validators import MaxValueValidator, MinValueValidator

from .matching import matching


GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('O', 'Other'),
    ('U', 'Prefer not to say'),
)

CLASS_RANK_CHOICES = (
    ('1', 'First Year'),
    ('2', 'Second Year'),
    ('3', 'Third Year'),
    ('4', 'Fourth Year'),
    ('G', 'Graduate Student'),
    ('U', 'Prefer not to say'),
)

POLITICAL_VIEW_CHOICES = (
    ('L', 'Liberal'),
    ('M', 'Moderate'),
    ('C', 'Conservative'),
    ('U', 'Prefer not to say'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #full_name = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='U')

    class_rank = models.CharField(
        max_length=1, choices=CLASS_RANK_CHOICES, default='U')

    major = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(
        default='default.jpg', upload_to='profile_pictures')
    description = models.TextField(max_length=300, blank=True)

    roommates = models.IntegerField(
        default=1, validators=[MinValueValidator(1)])
    semesters = models.IntegerField(
        default=2, validators=[MinValueValidator(1)])

    politics = models.CharField(
        max_length=1, choices=POLITICAL_VIEW_CHOICES, default='U')

    social_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    tidiness_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    party_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    guest_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])

    min_match_percentage = models.FloatField(
        default=75, validators=[MaxValueValidator(100.0), MinValueValidator(0.0)])

    match_enabled = models.BooleanField(default=False)

    matches = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.matches.clear()

        if self.match_enabled:
            match_profiles = Profile.objects.filter(match_enabled=True)

            for profile in match_profiles:
                if profile != self:
                    score = matching(self, profile)
                    if score > self.min_match_percentage and score > profile.min_match_percentage:
                        self.matches.add(profile)
                        profile.matches.add(self)

        super(Profile, self).save(force_insert, force_update, *args, **kwargs)

    @property
    def get_photo_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return "/static/img/default.jpg"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
