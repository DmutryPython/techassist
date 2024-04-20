from django.shortcuts import render, redirect
from .forms import userform, entrform
from .models import user, Room, Message
from django.views.generic import DetailView
from django.http import HttpResponse, JsonResponse


def registration(request):
    error = ''
    if request.method == 'POST':
        login = request.POST['login']
        form = userform(request.POST)
        if login in user.objects.values_list('login', flat=True):
            error = 'логин занят'
        else:
            if form.is_valid():
                form.save()
                return redirect('entr/')
            else:
                error = 'неверные данные'
    form = userform

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/registration.html', data)


def entr(request):
    error = ''
    if request.method == 'POST':
        if request.POST['reg_or'] == 'reg':
            return redirect('../')
        login = request.POST['login']
        password = request.POST['password']
        form = userform(request.POST)
        if login not in user.objects.values_list('login', flat=True):
            error = 'нет логина'
        else:
            password_user = user.objects.filter(login=login).values_list('password', flat=True).first()
            if str(password_user) != str(password):
                error = 'неверный пароль'
            else:
                data = {
                    'username': login
                }
                return render(request, 'main/home.html', {'login': login})
    form = entrform

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/entr.html', data)



def room(request, room):
    username = request.GET.get('username')
    product = user.objects.get(pk=username)
    product.appel = product.appel + ' ' + room
    product.save()
    room_details = Room.objects.get(name=room)
    return render(request, 'main/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('' + room + '/?username=' + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})


def profile(request):
    login = request.GET.get('username')
    login_details = user.objects.filter(pk=login).values_list('appel', flat=True).get()
    print(login_details)
    data = {
        'login': login,
        'appel': set(login_details.split())
    }
    return render(request, 'main/profile.html', data)