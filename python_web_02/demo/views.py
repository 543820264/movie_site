from django.shortcuts import render


# Create your views here.
def index(request):
    context = 'name'

    return render(request, 'index.html', {'hello': context})
