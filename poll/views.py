from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from . generators import cripto, descripto
from django.contrib.auth import authenticate, logout, login as auth_login
from . models import Aluno, Candidato, Candidata, Token
import secrets, random




# Create your views here.

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def register_candidates(request):
    if request.method == "GET":
        return render(request, 'register_candidates.html')
    else:
        print("CHEGOU ISSO: ", request.POST, request.FILES)
        name = request.POST.get('name')
        description = request.POST.get('description')
        number = request.POST.get('number')
        classroom = request.POST.get('classroom')
        photo = request.FILES.get('photo')
        sexo = request.POST.get('sexo')
        if name and description and number and classroom and photo and sexo:
            if sexo == "0":
                if Candidato.objects.filter(numero_do_candidato=number).exists():
                    messages.error(request, f'Algum candidato já possui esse número.')
                    return redirect('register-candidates')
                Candidato.objects.create(candidato=name,descricao_candidato=description,numero_do_candidato=number,turma_candidato=classroom,foto_candidato=photo)
                messages.success(request, f'Candidato {name} cadastrado com sucesso.')
            elif sexo == "1":
                if Candidata.objects.filter(numero_da_candidata=number).exists():
                    messages.error(request, f'Alguma candidata já possui esse número.')
                    return redirect('register-candidates')
                Candidata.objects.create(candidata=name,descricao_candidata=description,numero_da_candidata=number,turma_candidata=classroom,foto_candidata=photo)
                messages.success(request, f'Candidata {name} cadastrada com sucesso.')
            print("aa")
        return redirect('register-candidates')
    
def manage_candidates(request):
    pass

def gerar_token_20():
    token = secrets.token_urlsafe(20) 
    return token[:20]  

def votacao(request):
    if request.method == "GET":
        return render(request, 'votation.html')
    else:
        registration = request.POST.get('registration')
        cpf = request.POST.get('cpf')
        if Aluno.objects.filter(matricula=registration, cpf=cpf).exists():
            aluno = Aluno.objects.get(matricula=registration, cpf=cpf)
            if aluno.votou:
                messages.info(request, f"{aluno.nome} já votou.")
                return redirect('votacao')
            print("Votação liberada")
            code_token = gerar_token_20()
            number = random.randint(0, 39)
            if not Token.objects.filter(student=aluno).exists():
                token = Token.objects.create(student=aluno, token=code_token, number=number)
            else:
                token = Token.objects.get(student=aluno)
                token.delete()
                code_token = gerar_token_20()
                number = random.randint(0, 39)
                token = Token.objects.create(student=aluno, token=code_token, number=number)
            return redirect('candidato', token.token)
        else:
            print("Votação fechada")
            messages.error(request, "Matrícula e/ou CPF incorreto(s).")
            return redirect('votacao')

def candidato(request, id):
    if not Token.objects.filter(token=id).exists():
        messages.info(request, "Por segurança, reinicie o processo. Caso você já tenha escolhido o candidato os sistema identificará.")
        return redirect('votacao')
    else:
        token = Token.objects.get(token=id)
    aluno = Aluno.objects.get(id=token.student.id)
    if aluno.votou:
        messages.info(request, f"{aluno.nome} já votou.")
        return redirect('votacao')
    elif aluno.candidato != 0:
        token = Token.objects.get(student=aluno)
        token.token = gerar_token_20()
        token.save()
        messages.info(request, "Você ja escolheu o seu candidato, falta apenas a candidata.")
        return redirect('candidata', token.token)
    
    if request.method == "GET":
        print("aluno: ",aluno)
        return render(request, 'candidato.html',{'aluno': aluno})
    else:
        token = Token.objects.get(student=aluno)
        token.token = gerar_token_20()
        token.save()
        number = request.POST.get('number')
        if Candidato.objects.filter(numero_do_candidato=number).exists():
            candidato = Candidato.objects.get(numero_do_candidato=number)
            print("Votação liberada", candidato.candidato)
            messages.success(request, f"Candidato encontrado: {candidato.candidato}")
            number_str = cripto(int(token.number), str(candidato.numero_do_candidato))
            
            return redirect('confirmar', 1, number_str, token.token)
        else:
            messages.error(request,"Candidato não encontrado.")
            return redirect('candidato', token.token)

def candidata(request, id):
    if not Token.objects.filter(token=id).exists():
        messages.info(request, "Por segurança, reinicie o processo. Caso você já tenha escolhido o candidato os sistema identificará.")
        return redirect('votacao')
    else:
        token = Token.objects.get(token=id)
    aluno = Aluno.objects.get(id=token.student.id)
    if aluno.votou:
        messages.info(request, f"{aluno.nome} já votou.")
        return redirect('votacao')
    elif aluno.candidato == 0:
        messages.info(request, "Primeiro escolha o seu candidato.")
        return redirect('candidato', id)
    elif request.method == "GET":
        print("aluno: ",aluno)
        return render(request, 'candidata.html',{'aluno': aluno})
    else:
        token = Token.objects.get(student=aluno)
        token.token = gerar_token_20()
        token.save()
        number = request.POST.get('number')
        if Candidata.objects.filter(numero_da_candidata=number).exists():
            candidata = Candidata.objects.get(numero_da_candidata=number)
            print("Votação liberada", candidata.candidata)
            messages.success(request, f"Candidata encontrado: {candidata.candidata}")
            number_str = cripto(int(token.number), str(candidata.numero_da_candidata))
            
            return redirect('confirmar', 2, number_str, token.token)
        else:
            messages.error(request,"Candidata não encontrada.")
            return redirect('candidata', token.token)
        
def confirmar(request, number, candid, id):
    if not Token.objects.filter(token=id).exists():
        messages.info(request, "Por segurança, reinicie o processo. Caso você já tenha escolhido o candidato os sistema identificará.")
        return redirect('votacao')
    else:
        token = Token.objects.get(token=id)
    aluno = Aluno.objects.get(id=token.student.id)
    numero_int = descripto(int(token.number), str(candid))
    if number == 1: 
        candidate = Candidato.objects.get(numero_do_candidato=numero_int)
    else: 
        candidate = Candidata.objects.get(numero_da_candidata=numero_int)
    if request.method == "GET":
        return render(request, 'confirmar.html',{'aluno': aluno, 'candidate': candidate, 'number': number, 'token': token, 'candid': candid})
    else:
        return render(request, 'votation.html')
    
def confirmar_cand(request, number, candid, id):
    if not Token.objects.filter(token=id).exists():
        messages.info(request, "Por segurança, reinicie o processo. Caso você já tenha escolhido o candidato os sistema identificará.")
        return redirect('votacao')
    else:
        token = Token.objects.get(token=id)
    aluno = Aluno.objects.get(id=token.student.id)
    number_int = descripto(int(token.number), str(candid))
    if number == 1: 
        aluno.candidato = number_int
        aluno.save()
        token = Token.objects.get(student=aluno)
        token.number = random.randint(0, 39)
        token.save()
        messages.success(request, "Candidato escolhido com sucesso!")
        return redirect('candidata', token.token)
    else: 
        aluno.candidata = number_int
        aluno.votou = True
        aluno.save()
        Token.objects.get(student=aluno).delete()
        messages.success(request, "Votação finalizada!")
        return redirect('finalizacao')
    
def finalizacao(request):
    return render(request, 'finalizacao.html')  

def register_student(request):
    if request.method == "GET":
        return render(request, 'register_student.html')
    else:
        name = request.POST.get('name')
        registration = request.POST.get('registration')
        classroom = request.POST.get('classroom')
        if Aluno.objects.filter(matricula=registration).exists():
            messages.info(request, "Já existe um aluno com essa matrícula.")
            return redirect('register-student')
        Aluno.objects.create(nome=name, matricula=registration, turma=classroom)
    return redirect('register-student')

def manage_student(request):
    pass

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
    
def account_login(request):
    print("login")
    if not request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'login/login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                auth_login(request, user)
                return redirect('account-login')
            else:
                return redirect('account-login')
    return redirect('home')

def account_logout(request):
    logout(request)
    return redirect('home')

def validar_token(request, token_str):
    try:
        token = Token.objects.get(token=token_str)
        if token.valid():
            pass
        else:
            return redirect('votacao')
    except Token.DoesNotExist:
        return redirect('votacao')