from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1> Hello By Django In Docker! </h1>")
