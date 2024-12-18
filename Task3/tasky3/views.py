from django.shortcuts import render

def home(request):
       return render(request, 'third_task/platform.html')

def shop(request):
       games = {
           'Atomic Heart': 'Купить',
           'Cyberpunk 2077': 'Купить',
           'PayDay 2': 'Купить',
       }
       return render(request, 'third_task/games.html', {'games': games})

def cart(request):
       return render(request, 'third_task/cart.html')