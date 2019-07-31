from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class RegisterManager(BaseUserManager):
    # def _create_user(self, e_mail, password, is_staff, is_superuser, **extra_fields):
    #
    #     now = timezone.now()
        # if not e_mail:
        #     raise ValueError('Please give e-mail id to process')
        # e_mail = self.normalize_email(e_mail)
        # user = self.model(e_mail= e_mail, **extra_fields)
# last_login= now, date_joined= now,                  is_superuser= is_superuser, is_staff= is_staff, is_active= True,
        # user.set_password(password)
        # user.save(using=self._db)
        # return user

    def create_user(self, e_mail=None, password=None, **extra_fields):
        if not e_mail:
            raise ValueError('Please give e-mail id to process')
        e_mail = self.normalize_email(e_mail)
        user = self.model(e_mail= e_mail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, e_mail, password, **extra_fields):
        user = self.create_user(e_mail, password, **extra_fields)
        user.is_superuser= True;
        user.is_staff=True;
        user.save(using=self._db)
        return user

class Register(AbstractBaseUser):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100, unique=True)
    e_mail = models.EmailField(unique=True)
    skills = models.CharField(max_length = 256)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'e_mail'
    REQUIRED_FIELDS =['username']
# 'first_name', 'last_name', 'skills',

    objects = RegisterManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # def get_full_name(self):
    #     self.e_mail()

    def get_short_name(self):
        return self.e_mail

    def __str__(self):
        return self.e_mail

    def has_perm(self, perm, obj=None):

    # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):

    # Simplest possible answer: Yes, always
        return True
    #
    # def is_staff(self):
    #
    # # Simplest possible answer: All admins are staff
    #     return self.is_staff


class CodePost(models.model):
    description = models.TextField()
    name = models.CharField(max_length="125")
    ts = models.DateField(auto_now=True)
