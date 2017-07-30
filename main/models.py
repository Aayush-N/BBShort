from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Create your models here.

User = settings.AUTH_USER_MODEL

class URLTable(models.Model):
	class Meta:
		verbose_name = ("URL Table")
	id      = models.AutoField(primary_key=True)
	name    = models.CharField(max_length=50, null=False, default="No name")

	def __str__(self):
		return self.name
