from django.shortcuts import render
from django.http import  JsonResponse
import requests

RUN_URL = "http://api.hackerearth.com/code/run/"
CLIENT_SECRET_KEY = "***********************************"


def index(request):
    return render(request, "MainYoIde.html", {})


def compile_and_run(request):
    if request.method == "POST" and request.is_ajax():
        data = {
            'client_secret': CLIENT_SECRET_KEY,
            'async': 0,
            'source': request.POST.get("source", " "),
            'lang': request.POST.get("lang", ""),
            'time_limit': 5,
            'memory_limit': 262144,
        }
        if request.POST.get("input", ""):
            data['input'] = request.POST.get("input", "")
        response_data = requests.post(RUN_URL, data=data)
        return JsonResponse(response_data.json(), safe=False)
    else:
        return render(request, "error.html", {"test": " Oops bad request !! "})


def contact_us(request):
    return render(request, "Contact-us.html", {})


def feedback(request):
    return render(request, "feedback.html", {})

