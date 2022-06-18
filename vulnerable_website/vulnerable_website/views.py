from django.http import JsonResponse
from django.views import View

class SensitiveData(View):

    def get(self, request, *args, **kwargs):

        response = JsonResponse(f'This is sensitive data for user: {request.user}', safe=False)
        if 'Origin' in request.headers:
            response["Access-Control-Allow-Origin"] = request.headers['Origin']
        else:
            response["Access-Control-Allow-Origin"] = ""
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Credentials"] = "true"
        return response
