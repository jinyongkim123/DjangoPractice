from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    # # trigger 500 error
    pass
    #return HttpResponse("main index")

def error_404_view(request, exception):
    #return HttpResponseNotFound("The page is not found!")
    return render(request, '404.html')


def error_500_view(request, exception):
    return render(request, '500.html')