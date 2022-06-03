from django.contrib import admin
from accounts.models.ngouser import *
from accounts.models.userprofile import *
from accounts.models.otpdevices import VerificationDevice
from django.contrib.sessions.models import Session
from accounts.models.subscriptions import *
from mptt.admin import MPTTModelAdmin

admin.site.register(DetailPoint)

class DetailsInline(admin.TabularInline):
    model = DetailPoint

class DetailValueInline(admin.TabularInline):
    model = DetalPointValue

@admin.register(SubscriptionType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [DetailValueInline]

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class VerificationDeviceInline(admin.StackedInline):
    model = VerificationDevice

class ProfileImageInline(admin.StackedInline):
    model = ProfileImage

@admin.register(NGO_User)
class RadixAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline, VerificationDeviceInline]

@admin.register(UserProfile)
class RadixAdmin(admin.ModelAdmin):
    inlines = [ProfileImageInline]

admin.site.register(LoggedInUser)
admin.site.register(Session)