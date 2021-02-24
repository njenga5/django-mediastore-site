from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, Http404
import os
from django.contrib import messages
from django.utils import timezone
from . import forms
from . import models
from commonops.models import CustomUser as User

MUSIC_TYPES = ['mp3', 'ogg', 'm4a', 'wav', 'opus']
VIDEO_TYPES = ['mp4', 'webm',]
MAX_SPACE = 524_288_000


def dashboard_home(request):
    if 'user' in request.session:
        user_email = request.session['user']
        user = get_object_or_404(User, email=user_email)
        pictures = user.photo_set.order_by('-upload_date')
        musics = user.music_set.all()
        videos = user.video_set.all()
        pic_size = sum((picture.picture.size for picture in pictures))
        music_size = sum((music.track.size for music in musics))
        vids_size = sum((video.video.size for video in videos))
        context = {
            'pictures': pictures,
            'pic_size': pic_size,
            'music_size': music_size,
            'vids_size': vids_size,
            'total_size': sum((pic_size, music_size, vids_size)),
            'max_size': MAX_SPACE,
            'user': user,
        }
        if len(user.albumdescription_set.all()) > 0:
            context['title'] = \
                user.albumdescription_set.order_by('-created_at').first().title
            context['description'] = \
                user.albumdescription_set.order_by('-created_at').first().description
        if request.method == "POST":
            form = forms.AlbumDescriptionForm(request.POST)
            if form.is_valid():
                details = form.save(commit=False)
                details.user = user
                details.save()
                return redirect('dashboard:profile')
        return render(request, 'dashboard/album.html', context)
    return redirect('commonops:auth')


def upload_photo(request):
    form = forms.PhotoForm()
    if 'user' in request.session:
        if request.method == "GET":
            return render(request, 'dashboard/uploadphoto.html', {'form': form})

        elif request.method == "POST":
            form = forms.PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                user = User.objects.get(email=request.session['user'])
                photo = form.save(commit=False)
                photo.picture = form.cleaned_data.get('picture')
                photo.user = user
                photo.save()
                messages.success(request, f"Photo {photo.picture.url.split('/')[-1]} uploaded successfully.")
            return render(request, 'dashboard/uploadphoto.html', {'form': form, 'user': user})
        return render(request, 'dashboard/bad_request.html')
    return redirect('commonops:auth')


def upload_music(request):
    form = forms.MusicForm()
    if 'user' in request.session:
        if request.method == 'GET':
            return render(request, 'dashboard/uploadmusic.html', {'form': form})

        elif request.method == 'POST':
            form = forms.MusicForm(request.POST, request.FILES)
            if form.is_valid():
                user = User.objects.get(email=request.session['user'])
                music = form.save(commit=False)
                music.user = user
                music.track = form.cleaned_data.get('track')
                file_type = music.track.url.split('.')[-1]
                file_type.lower()
                if file_type not in MUSIC_TYPES:
                    return render(request, 'dashboard/errormusic.html', {'allowed_types': MUSIC_TYPES})
                music.save()
                messages.success(request, f"Track {music.track.url.split('/')[-1]} uploaded successfully")
            return render(request, 'dashboard/uploadmusic.html', {'form': form, 'user': user})
        return render(request, 'dashboard/bad_request.html')
    return redirect('commonops:auth')
    

def upload_video(request):
    form = forms.VideoForm()
    if 'user' in request.session:
        if request.method == 'GET':
            return render(request, 'dashboard/uploadvideo.html', {'form': form})

        elif request.method == 'POST':
            form = forms.VideoForm(request.POST, request.FILES)
            if form.is_valid():
                video = form.save(commit=False)
                user = User.objects.get(email=request.session['user'])
                video.user = user
                video.video = form.cleaned_data.get('video')
                file_type = video.video.url.split('.')[-1]
                file_type.lower()
                if file_type not in VIDEO_TYPES:
                    return render(request, 'dashboard/errorvideo.html', {'allowed_types': VIDEO_TYPES})
                video.save()
                messages.success(request, f"Video {video.video.url.split('/')[-1]} uploaded successfully")
            return render(request, 'dashboard/uploadvideo.html', {'form': form, 'user': user})
        return render(request, 'dashboard/bad_request.html')
    return redirect('commonops:auth')


def profile_details(request):
    if request.session.has_key('user'):
        user = get_object_or_404(User, email=request.session['user'])
        next_birthday = timezone.datetime(timezone.now().year, user.date_of_birth.month, user.date_of_birth.day)
        if timezone.make_aware(next_birthday) <= timezone.now():
            next_birthday = timezone.datetime(timezone.now().year + 1, user.date_of_birth.month, user.date_of_birth.day)
        return render(request, 'dashboard/profiledetail.html', {'user': user, 'birthday': next_birthday})
    else:
        return redirect('commonops:auth')

# TODO: Refactor this function to use tags
def add_to_collection(request, item_id, source):
    if 'user' in request.session:
        if request.method == 'POST':
            data = request.POST
            query_set_colls = models.Collection.objects.all()
            collection = models.Collection(name=data['collections'])
            if collection.name in (query.name for query in query_set_colls):
                collection = query_set_colls.get(name=data['collections'])
            else:
                collection.save()

            if source == 'vid':
                vid = get_object_or_404(models.Video, pk=item_id)
                vid.collections.add(collection)
                return HttpResponse(f'Video {vid.video.url.split("/")[-1]} added to collection: {data["collections"]}')

            elif source == 'music':
                music = get_object_or_404(models.Music, pk=item_id)
                music.collections.add(collection)
                return HttpResponse(
                    f'Track {music.track.url.split("/")[-1]} added to collection: {data["collections"]}')
            else:
                raise Http404
        return render(request, 'dashboard/bad_request.html', {})
    return redirect('commonops:auth')


def find_item(request, item, item_id):
    if 'user' in request.session:
        if request.method == 'GET':
            context = {
                'item':item,
                'item_id':item_id,
            }
            return render(request, 'dashboard/confirm_delete.html', context)            
        return render(request, 'dashboard/bad_request.html', {})
    return redirect('commonops:auth')

def delete_item(request, item, item_id):
    if 'user' in request.session:
        if request.method == 'GET':
            user = request.session['user']
            if item == 'pic':
                photo = get_object_or_404(models.Photo, user__email=user, id=item_id)
                path = photo.picture.path
                norm_path = os.path.splitext(path)[0].split('\\')
                try:
                    os.unlink(path)
                except NotImplementedError:
                    os.remove(path)
                photo.delete()
                context = {
                    'file':norm_path[-1],
                    'type':'Picture',
                }
            elif item == 'music':
                music = get_object_or_404(models.Music, user__email=user, id=item_id)
                path = music.track.path
                norm_path = os.path.splitext(path)[0].split('\\')
                try:
                    os.unlink(path)
                except NotImplementedError:
                    os.remove(path)
                music.delete()
                context = {
                    'file':norm_path[-1],
                    'type':'Track',
                }
            elif item == 'vid':
                video = get_object_or_404(models.Video, user__email=user, pk=item_id)
                path = video.video.path
                norm_path = os.path.splitext(path)[0].split('\\')
                try:
                    os.unlink(path)
                except NotImplementedError:
                    os.remove(path)
                video.delete()
                context = {
                    'file':norm_path[-1],
                    'type':'Video',
                }
            else:
                raise Http404
            return render(request, 'dashboard/delete_success.html', context)
        return render(request, 'dashboard/bad_request.html', {})
    return redirect('commonops:auth')

def edit_photo_view(request, pk):
    if 'user' in request.session:
        if request.method == 'GET':
            user = request.session.get('user')
            photo = get_object_or_404(models.Photo, user__email=user, id=pk)
            collections = photo.tags.all()
            context = {
                'photo': photo,
                'collections': collections,
                'user': photo.user
            }
            return render(request, 'dashboard/editphoto.html', context)

        elif request.method == "POST":
            print(request.POST)
    return redirect('commonops:auth')


def logout(request):
    try:
        request.session.clear_expired()
        request.session.flush()
    except Exception as e:
        pass
    return redirect('commonops:auth')
