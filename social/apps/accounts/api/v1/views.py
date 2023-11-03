from django.http import HttpResponse


def v1(request):
    return HttpResponse("Hello from v1")
