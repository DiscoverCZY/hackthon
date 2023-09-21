import json

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from .models import Location, wrap

response_dct = {
    "data": {
        "modal": "chart",
        "type": "bar",
        "name": "seris-1",
        "categories": [1991, 1992],
        "data": [30, 40],
    }
}


class ChatModalView(APIView):
    def get(self, request):
        return JsonResponse(response_dct)

    def post(self, request):
        return HttpResponse(response_dct)


class RunQueryView(APIView):
    def get(self, request):
        result = {"message": 'success', "code": '0', "data": []}
        # scripts = Scripts.objects.all()[0:1]
        # result["data"] = serializers.serialize('python', scripts)
        # query_set = models.ChatModal;
        return HttpResponse(json.dumps(result), content_type="application/json")

    def get_my_model_data(request):
        my_model_data = Location.objects.all()
        data = [{'name': item.name, 'description': item.description} for item in my_model_data]
        return JsonResponse({'data': data})


class WorkflowDeployView(APIView):

    def __pos__(self, request):
        if request.data is None or len(request.data) == 0:
            return JsonResponse(wrap(code=500, message='payload is required'))

        return JsonResponse(wrap(message='workflow has been created'))
