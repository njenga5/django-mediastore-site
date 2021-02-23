# import hashlib
# import binascii
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(_('Full Name'), max_length=150, null=False, blank=False)
    phone_number = models.CharField(_('Phone Number'), max_length=13, null=False, blank=False)
    is_staff = models.BooleanField(default=False,  help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')
    is_active = models.BooleanField(default=True,  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']
    EMAIL_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        '''
        Return a full name of the current user
        '''
        return self.full_name
    
    def get_short_name(self):
        '''
        Return the first name of the current user
        '''
        return "%s" % self.full_name.split()[0]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = False

