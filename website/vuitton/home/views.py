from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def legitima(request):
    return render(request, "home/legitima.html")

def process_token(request):
    if request.method == 'POST':
        # Get the submitted token from the form
        token = request.POST.get('token', '')

        # Here, you can process the 'token' as needed.
        # For this example, we'll just print it to the console.
        print(f"Received token: {token}")

        # You can perform any further actions with the token here.

        # After processing, you may want to redirect the user to a thank-you page or another page.
        # Replace 'thank_you' with the actual URL pattern or path.
        return HttpResponseRedirect('thank_you')

    # Handle GET requests or render the form again
    return render(request, 'legitima.html')
