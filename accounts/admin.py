from django.contrib import admin
from accounts.models.ngouser import *
from accounts.models.userprofile import *
from accounts.models.otpdevices import VerificationDevice
from django.contrib.sessions.models import Session

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class VerificationDeviceInline(admin.StackedInline):
    model = VerificationDevice

@admin.register(NGO_User)
class NGOAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline, VerificationDeviceInline]

admin.site.register(LoggedInUser)
admin.site.register(Session)