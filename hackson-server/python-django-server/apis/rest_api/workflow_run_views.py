from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from _databricks.workflow_run import start_workspace, load_list
from _lib.view import resp,resp_err

mock_data={"id":"xxx"}
ERROR_FAIL_LOAD_LIST='Internal Error: fail to load run list'
ERROR_FAIL_LOAD_LIST_CODE=100

class WorkflowRunView(APIView):
    def get(self, request):
        try:
            data = load_list(request)
            return resp(data)
        except Exception as e:
            return resp_err(ERROR_FAIL_LOAD_LIST,ERROR_FAIL_LOAD_LIST_CODE)
        

    def post(self, request):
        data = start_workspace(request.data)
        return resp(data)

    def put(self, request):
        return resp({})