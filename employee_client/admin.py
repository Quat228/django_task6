from django.contrib import admin
from . import models


admin.site.register(models.Employee)
admin.site.register(models.Passport)
admin.site.register(models.WorkProject)
admin.site.register(models.Membership)
admin.site.register(models.Client)
admin.site.register(models.VIPClient)
