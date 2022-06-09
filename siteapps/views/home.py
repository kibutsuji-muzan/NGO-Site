from django.shortcuts import render
from django.views import View

class IndexView(View):

    def get(self, request):
        try:
            del request.session['email']
        except:
            pass
        return render(request, 'index.html') 