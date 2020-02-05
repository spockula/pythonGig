# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .manager import UserManager
import uuid



# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

class Users(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null = False)
    email = models.EmailField(unique=True, null = False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    amount = models.CharField(max_length=100, null=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    password = models.CharField(max_length=255, null=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    userId = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
   
    objects = UserManager()

    username=None
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name', 'amount', 'gender']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
    
    def get_UserId(self):
        '''
        returns the Unique Id of the user.
        '''
        return self.userId

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email