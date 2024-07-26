from django.shortcuts import render
from django.http import JsonResponse
from . models import Aluno, Candidato, Candidata

# Create your views here.

def index(request):
    return render(request, 'index.html')

def candidates(request):
    return render(request, 'candidates.html')

def results(request):
    lista_de_candidatos = Candidato.objects.all()
    lista_de_candidatas = Candidata.objects.all()
    top_candidatos = Candidato.objects.order_by('-votos_do_candidato')[:3]
    top_candidatas = Candidata.objects.order_by('-votos_da_candidata')[:3]
    
    candidato_1 = top_candidatos[0] if len(top_candidatos) > 0 else None
    candidato_2 = top_candidatos[1] if len(top_candidatos) > 1 else None
    candidato_3 = top_candidatos[2] if len(top_candidatos) > 2 else None

    candidata_1 = top_candidatas[0] if len(top_candidatas) > 0 else None
    candidata_2 = top_candidatas[1] if len(top_candidatas) > 1 else None
    candidata_3 = top_candidatas[2] if len(top_candidatas) > 2 else None

    def calcular_porcentagem(value, total):
        if total == 0:
            return 0
        return f'{((value / total) * 100):5.1f}'
        

    candidatos_total= candidato_1.votos_do_candidato + candidato_2.votos_do_candidato + candidato_3.votos_do_candidato
    porcentanditato1 = calcular_porcentagem(candidato_1.votos_do_candidato, candidatos_total)
    porcentanditato2 = calcular_porcentagem(candidato_2.votos_do_candidato, candidatos_total)
    porcentanditato3 = calcular_porcentagem(candidato_3.votos_do_candidato, candidatos_total)

    candidatas_total= candidata_1.votos_da_candidata + candidata_2.votos_da_candidata + candidata_3.votos_da_candidata
    porcentanditata1 = calcular_porcentagem(candidata_1.votos_da_candidata, candidatas_total)
    porcentanditata2 = calcular_porcentagem(candidata_2.votos_da_candidata, candidatas_total)
    porcentanditata3 = calcular_porcentagem(candidata_3.votos_da_candidata, candidatas_total)
    
    

    context = {
        'lista_de_candidatos': lista_de_candidatos,
        'lista_de_candidatas': lista_de_candidatas,
        'candidato_1': candidato_1,
        'candidato_2': candidato_2,
        'candidato_3': candidato_3,
        'candidata_1': candidata_1,
        'candidata_2': candidata_2,
        'candidata_3': candidata_3,
        'porcentanditato1': porcentanditato1,
        'porcentanditato2': porcentanditato2,
        'porcentanditato3': porcentanditato3,
        'porcentanditata1': porcentanditata1,
        'porcentanditata2': porcentanditata2,
        'porcentanditata3': porcentanditata3,

    }
    pagina_rei_liberada = any(candidato.votos_do_candidato > 0 for candidato in lista_de_candidatos)
    pagina_rainha_liberada = any(candidata.votos_da_candidata > 0 for candidata in lista_de_candidatas)
    if pagina_rei_liberada and pagina_rainha_liberada:
        return render(request, 'results.html', context)
    else:
        return render(request, 'result-pendent.html') 
    
#api
def contabilizar_votos(request):
    matricula = request.GET.get('matricula')
    numero_do_candidato = request.GET.get('numero_voto_candidato')
    numero_da_candidata = request.GET.get('numero_voto_candidata')
    if not matricula or not numero_do_candidato or not numero_da_candidata:
        return JsonResponse({'error':'Matricula e os números dos candidatos são obrigatorios'}, status=400)
    try:
        aluno = Aluno.objects.get(matricula=matricula)
        if aluno.votou:
            return JsonResponse({'error':'aluno já votou'},status=400)
        candidato = Candidato.objects.get(numero_voto_candidato=numero_do_candidato)
        candidata = Candidata.objects.get(numero_voto_candidata=numero_da_candidata)
        Aluno.votou = True
        
        Aluno.save()
        
        Candidato.votos_do_candidato += 1
        Candidato.save()
        Candidata.votos_da_candidata += 1
        Candidata.save()
        return JsonResponse({'success':'Voto contabilizado com sucesso'},status=200)
    except Aluno.DoesNotExist:
        return JsonResponse({'error':'Matricula não encontrada'}, status=404)   