from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db                  import models

class UserManager(BaseUserManager):
    def _create_user(self, email, username, phone_number, password, **extra_fields):
        if not email :
            raise ValueError('The given email mist be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        phone_number = self.phone_number
        user = self.model(email = email,username=username, **extra_fields)
        user.set_password(password)
        user.save (using = self._db)
        return user

    def create_user(self, email, usernmae='', password = None, phone_number='', **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,username, phone_number, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        username = 'admin'
        phone_number= ''

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(email, username, password, **extra_fields)

class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    email        = models.EmailField(max_length=50, unique=True)
    password     = models.CharField(max_length=150)
    username     = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address      = models.CharField(max_length=200, null=True, blank=True)
    gender       = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
