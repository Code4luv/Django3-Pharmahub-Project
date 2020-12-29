from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, role, password=None):
        if not email:
            raise ValueError(" Please enter the username")
        if not username:
            raise ValueError("Please enter the username")
        if not role:
            raise ValueError(" Please select the role")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email), username=username, role='D', password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    roles = (('D', 'Doctor'), ('S', 'Shopkeeper'), ('U', 'User'))

    role = models.CharField(max_length=1, choices=roles)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email', 'role']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
