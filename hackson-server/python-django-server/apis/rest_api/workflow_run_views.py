from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from _databricks.workflow_run import start, load_list
from _lib.view import resp, resp_err
import traceback

mock_data={"id":"xxx"}
ERROR_FAIL_LOAD_LIST='Internal Error: fail to load run list'
ERROR_FAIL_LOAD_LIST_CODE=100

ERROR_FAIL_START='Internal Error: fail to start run'
ERROR_FAIL_START_CODE=100

class WorkflowRunView(APIView):
    def get(self, request):
        try:
            data = load_list(request)
            return resp(data)
        except Exception as e:
            traceback.print_exc()
            return resp_err(e,ERROR_FAIL_LOAD_LIST_CODE)
        

    def post(self, request):
        try:
            data = start(request.data)
            return resp(data)
        except Exception as e:
            traceback.print_exc()
            return resp_err(e,ERROR_FAIL_START_CODE)

    def put(self, request):
        return resp({})