import uuid 
from django.db import models
from datetime import datetime 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone 
from django.utils.translation import gettext_lazy as _ 

from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    """ user mod """
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(verbose_name=_("first name"), max_length=50)
    last_name = models.CharField(verbose_name=_("last name"), max_length=50)
    email = models.EmailField(verbose_name=_("email address"), db_index=True, unique=True, max_length=250)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    object = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    def __str__(self):
        return self.firstname
    
    @property 
    def get_full_name(self):
        return f"{self.firstname.title()}, {self.lastname.title()}"

    @property 

    def get_first_name(self):
        return self.first_name 
    




