from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Olá estranho, Sou eu..o Fabio Tanikawa!!!")