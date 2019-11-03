from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    """
    Stores a single User entry with basic customer fields.

    def save also slugify 'slug' field.
    """

    # constants for user user fields
    GENDERS = (
        (None, '-'),
        ('M', 'Male'),
        ('F', 'Female'),
    )

    HOBBIES = (
        ('sport', 'Sport'),
        ('games', 'Computer Games'),
    )

    # user custom fields
    address = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    phone = models.IntegerField(
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=20,
        null=True,
        default=''
    )
    bonuses = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        default=None,
        null=True
    )
    photo = models.ImageField(
        default='user/images/user_default.jpg',
        null=True
    )
    about = models.TextField(
        null=True,
        blank=True
    )
    age = models.IntegerField(
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=12,
        choices=GENDERS,
        default=None,
        null=True,
        blank=True
    )
    birthday = models.DateField(
        null=True,
        blank=True
    )
    hobbie = models.CharField(
        max_length=20,
        choices=HOBBIES,
        default='Sport',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save()

    def __str__(self):
        return self.username

    def has_permission(self):
        return self.is_superuser

    class Meta:
        unique_together = ['username', 'email']
