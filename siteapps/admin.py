from django.contrib import admin
from siteapps.models import donation
from siteapps.models.donation import * 
from siteapps.models.extras import * 
# Register your models here.

admin.site.register(donation)
admin.site.register(feedback)