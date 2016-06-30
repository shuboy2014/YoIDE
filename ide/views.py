from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.

RUN_URL = "http://api.hackerearth.com/code/run/"
CLIENT_SECRET_KEY="fc9bab4fc37aeeb507292c2c5a59e008ee8d345b"


def index(request):
    return render(request,"MainYoIde.html", {})


def compile_and_run(request):
    print request.method
    print request.is_ajax()
    if request.method == "POST" and request.is_ajax():
        return JsonResponse({"name" : "vijay chutiya"})
    else:
        return HttpResponse('<h1>Hello these , its Compile code request . </h1>')


def contact_us(request):
    return HttpResponse('<h1>We will connect to you shortly .</h1>')


def feedback(request):
    return HttpResponse('<h1>We will connect to you shortly .</h1>')

