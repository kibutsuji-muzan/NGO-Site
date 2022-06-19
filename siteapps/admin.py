from django.contrib import admin
from siteapps.models import donation
from siteapps.models.donation import * 
from siteapps.models.extras import * 
from siteapps.models.subscriptions import *
# Register your models here.

admin.site.register(DetailPoint)

class DetailsInline(admin.TabularInline):
    model = DetailPoint

class DetailValueInline(admin.TabularInline):
    model = DetailPointValue

@admin.register(SubscriptionType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [DetailValueInline]

admin.site.register(donation)
admin.site.register(feedback)