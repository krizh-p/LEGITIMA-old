from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Token
from .encrypt import encrypt, decrypt

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def legitima(request):
    return render(request, "home/legitima.html")

def loadToken(request, data):
    return render(request, "home/token.html", {
        "data" : data
    })

def report(request):
    return render(request, "home/report.html")

def invalid_token(request):
    return render(request, "home/invalid_token.html")

def thank_you(request):
    return render(request, "home/thank_you.html")

def process_token(request):
    if request.method == 'POST':
        # Get the submitted token from the form
        token = request.POST.get('token', '')
        # Search for a Token with a matching primary key
        try:
            token_instance = Token.objects.get(pk=token)
            return loadToken(request, token_instance)
        except Token.DoesNotExist:
            return render(request, "home/invalid_token.html")
            
    # Handle GET requests or render the form again
    return render(request, 'legitima.html')
