from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from commonops.models import CustomUser as User


def play_audio_view(request):
    if request.method == 'GET':
        if 'user' in request.session:
            user_email = request.session.get('user')
            user = get_object_or_404(User, email=user_email)
            musics = user.music_set.order_by('-upload_date')
            context = {
                'musics': {'audio': list({'audio': music.track.url,
                                           'songname': music.title,
                                           'thumbnail': music.art.url,
                                           'id': music.id,
                                           'artistname': music.artist} for music in musics)},
            }
            if request.GET.get('player') == 'alt-player':
                request.session['player'] = 'alt-player'
                return render(request, 'player/alt-player.html', context)
            request.session['player'] = ''
            return render(request, 'player/audioplayer.html', context)
        return redirect('commonops:auth')
    return render(request, 'player/forbidden.html')


def play_video_view(request):
    if request.method == 'GET':
        if 'user' in request.session:
            user_email = request.session.get('user')
            user = get_object_or_404(User, email=user_email)
            videos = user.video_set.order_by('-upload_date')
            context = {
                'urls': {'sources':[{'src': obj.video.url,
                                    'type': 'video/'+obj.video.url.split('.')[-1],
                                    'title': obj.title,
                                    'poster': obj.thumbnail.url,
                                    'artist':obj.artist} for obj in videos]},
                'videos': videos,
            }
            return render(request, 'player/videoplayer.html', context)
        return redirect('commonops:auth')
    return render(request, 'player/forbidden.html')
