from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def candidates(request):
    return render(request, 'candidates.html')

def resultpendent(request):
    return render(request, 'result-pendent.html')

def results(request):
    return render(request, 'results.html')