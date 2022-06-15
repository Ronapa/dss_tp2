from django.http import JsonResponse
from django.views import View

class SensitiveData(View):

    def get(self, request, *args, **kwargs):
        response = JsonResponse(f'This is sensitive data for user: {request.user}', safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        return response