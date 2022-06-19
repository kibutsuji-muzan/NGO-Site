from django.shortcuts import render
from django.views import View
from siteapps.models.subscriptions import SubscriptionType
class IndexView(View):

    def get(self, request):
        try:
            del request.session['email']
        except:
            pass

        subs = SubscriptionType.objects.all()
        
        return render(request, 'index.html', {"subsType":subs})