from django.shortcuts import render, redirect
from .models import Videos
from django.core.files.storage import FileSystemStorage


def home_page(request):
    return render(request, 'main/home.html')


def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        video = request.FILES['video']
        fs = FileSystemStorage()
        filename = fs.save(video.name, video)

        content = Videos(title=title, video=video)
        content.save()
        return redirect('show-videos')

    return render(request, 'main/video-upload.html')


def display(request):
    videos = Videos.objects.all()
    context = {
        'videos': videos,
    }

    return render(request, 'main/video-show.html', context)
