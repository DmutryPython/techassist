from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import quiz

def quiz_func(request):
    id = '1'
    text = quiz.objects.filter(id=id).values_list('text', flat=True).first()

    if request.method == 'POST':
        if request.POST['bot_or'] == 'oper':
            return redirect('registration/entr/')
        id = request.POST['id']
        yes_or_no = request.POST['quest']
        print(id, yes_or_no)
        answer = quiz.objects.filter(id=id).values_list(yes_or_no, flat=True).first()
        if answer[0] == 'q':
            id = answer[1:]
            text = quiz.objects.filter(id=id).values_list('text', flat=True).first()
        else:
            data = {
                'text': answer[1:]
            }
            return render(request, 'quiz/solut.html', data)


    data = {
        'id': id,
        'text': text
    }

    return render(request, 'quiz/quiz.html', data)
