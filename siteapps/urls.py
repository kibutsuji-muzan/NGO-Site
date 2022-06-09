from django.urls import path
from siteapps.views import home

urlpatterns = [
    path('', home.IndexView.as_view(), name='index')
]
