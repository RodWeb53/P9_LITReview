from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUserManager(BaseUserManager):

    def create_user(self, username, password=None, **Kwargs):
        if not username:
            raise ValueError("Vous devez entrer un nom d'utilisateur")
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomeUser(AbstractBaseUser):
    username = models.CharField(
        unique=True,
        max_length=128,
        blank=False,
        verbose_name="Nom d'utilisateur"
    )
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suivi',
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    