from django.shortcuts import render
from django.http import JsonResponse
from . models import Aluno, Candidato, Candidata

# Create your views here.

def index(request):
    return render(request, 'index.html')

def candidates(request):
    perfil_candidato = Candidato.objects.all()
    perfil_candidata = Candidata.objects.all()
    return render(request, 'candidates.html',{'perfil_candidato': perfil_candidato, 'perfil_candidata': perfil_candidata})

def results(request):
    lista_de_candidatos = Candidato.objects.all()
    lista_de_candidatas = Candidata.objects.all()

    # Obtém os 3 candidatos e candidatas com mais votos
    top_candidatos = list(Candidato.objects.order_by('-votos_do_candidato'))
    top_candidatas = list(Candidata.objects.order_by('-votos_da_candidata'))

    # Seleciona até 3 candidatos e candidatas, mesmo se houver menos de 3
    top_candidatos = top_candidatos[:3]
    top_candidatas = top_candidatas[:3]

    def calcular_porcentagem(value, total):
        if total == 0:
            return 0
        return round((value / total) * 100, 1)

    # Inicializando variáveis de porcentagem
    porcentanditato1 = porcentanditato2 = porcentanditato3 = 0
    porcentanditata1 = porcentanditata2 = porcentanditata3 = 0

    # Calculando a soma total dos votos para candidatos e candidatas
    candidatos_total = sum(c.votos_do_candidato for c in top_candidatos)
    candidatas_total = sum(c.votos_da_candidata for c in top_candidatas)

    # Calculando porcentagens para candidatos, se houver votos
    if candidatos_total > 0:
        for i, candidato in enumerate(top_candidatos):
            if i == 0:
                porcentanditato1 = calcular_porcentagem(candidato.votos_do_candidato, candidatos_total)
            elif i == 1:
                porcentanditato2 = calcular_porcentagem(candidato.votos_do_candidato, candidatos_total)
            elif i == 2:
                porcentanditato3 = calcular_porcentagem(candidato.votos_do_candidato, candidatos_total)

    # Calculando porcentagens para candidatas, se houver votos
    if candidatas_total > 0:
        for i, candidata in enumerate(top_candidatas):
            if i == 0:
                porcentanditata1 = calcular_porcentagem(candidata.votos_da_candidata, candidatas_total)
            elif i == 1:
                porcentanditata2 = calcular_porcentagem(candidata.votos_da_candidata, candidatas_total)
            elif i == 2:
                porcentanditata3 = calcular_porcentagem(candidata.votos_da_candidata, candidatas_total)

    # Adicionando candidatos e candidatas ao contexto
    context = {
        'lista_de_candidatos': lista_de_candidatos,
        'lista_de_candidatas': lista_de_candidatas,
        'candidato_1': top_candidatos[0] if len(top_candidatos) > 0 else None,
        'candidato_2': top_candidatos[1] if len(top_candidatos) > 1 else None,
        'candidato_3': top_candidatos[2] if len(top_candidatos) > 2 else None,
        'candidata_1': top_candidatas[0] if len(top_candidatas) > 0 else None,
        'candidata_2': top_candidatas[1] if len(top_candidatas) > 1 else None,
        'candidata_3': top_candidatas[2] if len(top_candidatas) > 2 else None,
        'porcentanditato1': porcentanditato1,
        'porcentanditato2': porcentanditato2,
        'porcentanditato3': porcentanditato3,
        'porcentanditata1': porcentanditata1,
        'porcentanditata2': porcentanditata2,
        'porcentanditata3': porcentanditata3,
    }

    pagina_rei_liberada = any(c.votos_do_candidato > 0 for c in lista_de_candidatos)
    pagina_rainha_liberada = any(c.votos_da_candidata > 0 for c in lista_de_candidatas)

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