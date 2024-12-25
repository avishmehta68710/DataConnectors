from django.db import models

from .base import BaseModel


class AddressModel(BaseModel):
	city = models.CharField(max_length=255, blank=True, null=True)
	state = models.CharField(max_length=255, blank=True, null=True)
	zip_code = models.CharField(max_length=255, blank=True, null=True)
	country = models.CharField(max_length=255, blank=True, null=True)
	type = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return f'{self.city}, {self.state} {self.zip_code}, {self.country}'
	