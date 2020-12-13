from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from commonops.models import User

@csrf_exempt
def play_audio_view(request, *args, **kwargs):
    if request.method == 'GET':
        if 'user' in request.session:
            user_email = request.session.get('user')
            user = get_object_or_404(User, pk=user_email)
            musics = user.music_set.order_by('-upload_date')
            videos = user.video_set.order_by('-upload_date')
            context = {
                'musics': {'audio': list(music.track.url for music in musics)},
                'videos': videos,
            }
            return render(request, 'player/audioplayer.html', context)
        return redirect('commonops:auth')
    return render(request, 'player/forbiden.html')