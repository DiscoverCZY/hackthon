import json

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from .models import wrap,Customer
from _langchain.langchain_db import run_query_with_nlp

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
        # if request.data is None or len(request.data) == 0:
            # return JsonResponse(wrap(code=500, message='payload is required'))
        # result = {"message": 'success', "code": '0', "data": []}
        # question = "get first 10 customer information and show columns id, name, phone, email, address, postal, region, country, sex, age"
        #question = "get 10 customer who's name start with A and show columns id, name, phone, email, address, postal, region, country, sex, age"
        question_suffix = "and show columns id, name, phone, email, address, postal, region, country, sex, age"
        customers = run_query_with_nlp(question)
        print("test====", customers.__len__)
        # result["data"] = serializers.serialize('python', customers,ensure_ascii=False)
        return JsonResponse(wrap(customers))
    
    def post(self, request):
        if request.data is None or len(request.data) == 0:
            return JsonResponse(wrap(code=500, message='payload is required'))
        question = str(request.data.get('question'))
        # result = {"message": 'success', "code": '0', "data": []}
        # question = "get first 10 customer information and show columns id, name, phone, email, address, postal, region, country, sex, age"
        #question = "get 10 customer who's name start with A and show columns id, name, phone, email, address, postal, region, country, sex, age"
        question_suffix = "and show columns id, name, phone, email, address, postal, region, country, sex, age"
        final_question = question + " " + question_suffix
        print(final_question)
        customers = run_query_with_nlp(final_question)
        # result["data"] = serializers.serialize('python', customers,ensure_ascii=False)
        return JsonResponse(wrap(customers))

        
        # return JsonResponse(wrap(message='workflow has been created'))


class WorkflowDeployView(APIView):

    def __pos__(self, request):
        if request.data is None or len(request.data) == 0:
            return JsonResponse(wrap(code=500, message='payload is required'))
        
        return JsonResponse(wrap(message='workflow has been created'))