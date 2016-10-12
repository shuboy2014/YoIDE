from django.shortcuts import render
from django.http import  JsonResponse
import requests

RUN_URL = "http://api.hackerearth.com/code/run/"
CLIENT_SECRET_KEY = "fc9bab4fc37aeeb507292c2c5a59e008ee8d345b"


def index(request):
    updatehits()
    return render(request, "MainYoIde.html", {})


# update hits
def updatehits():
    hit = Hits.objects.filter(date=datetime.date.today())
    if hit:
        hit_object = hit[0]
        hit_object.hits += 1
        hit_object.save()
    else:
        hit_object = Hits.objects.create(date=datetime.date.today())
        hit_object.hits += 1
        hit_object.save()
    return


def compile_and_run(request):
    updatehits()
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
    updatehits()
    return render(request, "Contact-us.html", {})


def feedback(request):
    updatehits()
    return render(request, "feedback.html", {})

