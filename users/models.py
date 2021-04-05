import datetime
from django.db import models
from django.contrib.auth.models import User, AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.validators import MaxValueValidator, MinValueValidator

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
    ('4', 'Four Year'),
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
    picture = models.ImageField(blank=True)
    description = models.TextField(max_length=300, blank=True)

    roommates = models.IntegerField(
        default=1, validators=[MinValueValidator(1)])
    semesters = models.IntegerField(
        default=2, validators=[MinValueValidator(1)])

    bedtime = models.TimeField(default=datetime.time(0, 0, 0))

    politics = models.CharField(
        max_length=1, choices=POLITICAL_VIEW_CHOICES, default='U')
    tidiness_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    party_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    guest_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
