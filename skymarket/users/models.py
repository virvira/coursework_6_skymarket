from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager, UserRoles


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=6, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to="avatars", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN  #

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)
    #     return super().save(*args, **kwargs)

