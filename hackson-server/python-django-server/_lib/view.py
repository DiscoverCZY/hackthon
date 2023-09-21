from django.http import JsonResponse

def resp(data):
    resp = {"data":data,"code":"111"}
    return JsonResponse(resp, safe=False)
