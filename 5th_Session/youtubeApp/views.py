from django.shortcuts import render
from .models import Channel

# Create your views here.
def main(request):
    channels = Channel.objects
    return render(request, 'main.html', {'channels':channels})