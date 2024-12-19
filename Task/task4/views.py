from django.shortcuts import render

def home(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077']}
    return render(request, 'fourth_task/home.html', context)

def platform(request):
    return render(request, 'fourth_task/platform.html')

def games (request):
       games = {
           'Atomic Heart': 'Купить',
           'Cyberpunk 2077': 'Купить',
           'PayDay 2': 'Купить',
       }
       return render(request, 'fourth_task/games.html', {'games': games})

def cart(request):
       return render(request, 'fourth_task/cart.html')