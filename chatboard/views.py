from django.shortcuts import render


def borad_list(request):
    return render(request, 'chatboard/board_list.html', {})

# Create your views here.
