from django.shortcuts import render,get_object_or_404,redirect
from .models import Channel

# Create your views here.
def main(request):
    channels = Channel.objects
    return render(request, 'main.html', {'channels':channels})

def detail(request, detail_id):
    detail = get_object_or_404(Channel, pk=detail_id)
    return render(request,'detail.html',{'content':detail})

def create(request):
    channels = Channel()
    channels.name = request.POST['name']
    channels.creator = request.POST['creator']
    channels.subscription = request.POST['subscribe_num']
    channels.link1 = request.POST['youtube_link_1']
    channels.link2 = request.POST['youtube_link_2']
    channels.link3 = request.POST['youtube_link_3']
    channels.summary = request.POST['summary']
    channels.text = request.POST['text']
    channels.live = request.POST['choices']
    channels.save()
    return redirect('main')

def new(request):
    return render(request, 'create.html')