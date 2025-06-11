from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('candidates/', views.candidates, name="candidates"),
    path('menu/', views.menu, name="menu"),
    path('results/', views.results, name="results"),
    path('api/receivedata', views.contabilizar_votos, name="receive-data"),

    path('accounts/login', views.account_login, name="account-login"),
    path('accounts/logout', views.account_logout, name="account-logout"),

    path('votacao', views.votacao, name="votacao"),
    path('candidato/<str:id>', views.candidato, name="candidato"),
    path('candidata/<str:id>', views.candidata, name="candidata"),
    path('confirmar/<int:number>/<str:candid>/<str:id>', views.confirmar, name="confirmar"),
    path('confirmar_cand/<int:number>/<str:candid>/<str:id>', views.confirmar_cand, name="confirmar_cand"),
    path('finalizacao', views.finalizacao, name="finalizacao"),

    path('register/candidates', views.register_candidates, name="register-candidates"),
    path('register/student', views.register_student, name="register-student"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)