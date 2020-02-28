from django.http import HttpResponse 

def index(request, *args, **kwargs):
    return HttpResponse('Hello, world. You re at the qa index.')

def login(request, *args, **kwargs):
    return HttpResponse('You re at the qa login')

def signup(request, *args, **kwargs):
    return HttpResponse('You re at the qa signup')

def question(request, *args, **kwargs):
    return HttpResponse('You re at the qa question')

def ask(request, *args, **kwargs):
    return HttpResponse('You re at the qa ask')

def popular(request, *args, **kwargs):
    return HttpResponse('You re at the qa popular')

def new(request, *args, **kwargs):
    return HttpResponse('You re at the qa new')





