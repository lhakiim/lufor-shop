from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Luqmanul Hakim',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)