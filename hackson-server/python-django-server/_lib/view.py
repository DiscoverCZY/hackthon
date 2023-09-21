from django.http import JsonResponse

def resp(data):
    resp = {"data":data,"code":0}
    return JsonResponse(resp, safe=False)

def resp_err(code, message):
    resp = {"data":{},"code":code, "message":message}
    return JsonResponse(resp, safe=False)
