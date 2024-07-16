from django.shortcuts import render
from django.http import JsonResponse
from . models import Aluno, Candidato, Candidata

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
    numero_candidato = request.GET.get('numero_voto_candidato')
    numero_candidata = request.GET.get('numero_voto_candidata')
    if not matricula or not numero_candidato or not numero_candidata:
        return JsonResponse({'error':'Matricula e os números dos candidatos são obrigatorios'}, status=400)
    try:
        aluno = Aluno.objects.get(matricula=matricula)
        if aluno.votou:
            return JsonResponse({'error':'aluno já votou'},status=400)
        candidato = Candidato.objects.get(numero_voto_candidato=numero_candidato)
        candidata = Candidata.objects.get(numero_voto_candidata=numero_candidata)
        Aluno.votou = True
        Aluno.save()
        Candidato.votos_candidato += 1
        Candidato.save()
        Candidata.votos_candidata += 1
        Candidata.save()
        return JsonResponse({'success':'Voto contabilizado com sucesso'},status=200)
    except Aluno.DoesNotExist:
        return JsonResponse({'error':'Matricula não encontrada'}, status=404)
