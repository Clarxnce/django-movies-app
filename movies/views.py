from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'movies': ['Spiderverse', 'Interstellar', 'Avengers Endgame']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    context = {}
    return render(request, 'movies/about.html', context)