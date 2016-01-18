from django.shortcuts import redirect
from django.shortcuts import render
from perfis.models import Convite
from perfis.models import Perfil
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden

@login_required
def index(request):   
    return render(request, 'index.html', {'perfis': Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request)})

@login_required
def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    jah_eh_contato = perfil in perfil_logado.contatos.all()	
    return render(request, 'perfil.html', {"perfil": perfil, "jah_eh_contato": jah_eh_contato})

@login_required
@permission_required('perfis.add_convite', raise_exception=True)
def convidar(request, perfil_id):
    if not request.user.has_perm('perfis.add_convite'):
        return HttpResponseForbidden('Acesso negado!')

    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')

@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')

@login_required
def get_perfil_logado(request):
    return request.user.perfil