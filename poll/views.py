from django.shortcuts import render
from django.http import JsonResponse
from . models import Aluno, Voto

# Create your views here.

def index(request):
    return render(request, 'index.html')

def candidates(request):
    return render(request, 'candidates.html')

def resultpendent(request):
    return render(request, 'result-pendent.html')

def results(request):
    return render(request, 'results.html')

def contabilizar_votos(request):
    matricula = request.GET.get('matricula')
    numero_candidato = request.GET.get('numero_candidato')
    if not matricula or not numero_candidato:
        return JsonResponse({'error':'Matricula e número do candidato são obrigatorios'}, status=400)
    try:
        aluno = Aluno.objects.get(matricula=matricula)
        if aluno.votou:
            return JsonResponse({'error':'aluno já votou'},status=400)
        
        Voto.objects.create(numero_candidato=numero_candidato)
        aluno.votou =True
        aluno.save()
        return JsonResponse({'success':'Voto contabilizado com sucesso'},status=200)
    except Aluno.DoesNotExist:
        return JsonResponse({'error':'Matricula não encontrada'}, status=404)
