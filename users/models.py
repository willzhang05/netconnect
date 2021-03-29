from django.db import models
from django.contrib.auth.models import AbstractUser

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


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='U')

    class_rank = models.CharField(
        max_length=1, choices=CLASS_RANK_CHOICES, default='U')

    major = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(blank=True)
    description = models.TextField(max_length=300, blank=True)

    politics = models.CharField(
        max_length=1, choices=POLITICAL_VIEW_CHOICES, default='U')
    tidiness_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    party_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    guest_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    sleep_late_factor = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
