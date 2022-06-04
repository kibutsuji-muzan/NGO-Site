from django.contrib import admin
from main.models import donation
from main.models.donation import * 
from main.models.extras import * 
# Register your models here.

admin.site.register(donation)
admin.site.register(feedback)