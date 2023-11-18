from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def school(request):
    return render(request, 'main/school.html')


def school_cite(request):
    return render(request, 'main/school_cite.html')


def school_game(request):
    return render(request, 'main/school_game.html')


def school_2(request):
    return render(request, 'main/school_2.html')


def school_3(request):
    return render(request, 'main/school_3.html')


def school_google(request):
    return render(request, 'main/school_google.html')


def school_inshe(request):
    return render(request, 'main/school_inshe.html')


def school_cite_2(request):
    return render(request, 'main/school_cite_2.html')


def school_inshe_2(request):
    return render(request, 'main/school_inshe_2.html')


def school_game_2(request):
    return render(request, 'main/school_game_2.html')


def school_all(request):
    return render(request, 'main/school_all.html')


def school_all_2(request):
    return render(request, 'main/school_all_2.html')