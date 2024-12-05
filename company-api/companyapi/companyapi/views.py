from django.http import HttpResponse


def home(request):
    print('Home view')
    return HttpResponse('<h1>Company API</h1>')