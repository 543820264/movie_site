from django.shortcuts import render,HttpResponse

def index(request):
    result = 'hello'
    return render(request, 'cms/index.html', {'rs': result})
# Create your views here.
