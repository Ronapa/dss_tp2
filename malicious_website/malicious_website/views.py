from django.http import HttpResponse
from django.views import View

class CapturedData(View):

    def get(self, request, *args, **kwargs):
        response = HttpResponse(request.__dict__)
        return response