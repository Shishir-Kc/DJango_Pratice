from django.contrib import admin

from . import models

admin.site.register(models.UserAccount)
admin.site.register(models.UserProfile)
admin.site.register(models.Admin)
admin.site.register(models.School_class)