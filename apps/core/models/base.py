from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """AbstractModel class"""

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class AbstractUserBaseModel(AbstractUser, BaseModel):
    """AbstractUser BaseModel class"""

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True
