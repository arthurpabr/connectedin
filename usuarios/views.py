from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from usuarios.forms import RegistrarUsuarioForm
from perfis.models import Perfil

# Criando uma class-based-view
class RegistrarUsuarioView(View):

	template_name = 'registrar.html'
	
	#renderiza o formulario
	def get(self, request):
		return render(request, self.template_name)

	#trata o submit do formulario
	def post(self, request):
		form = RegistrarUsuarioForm(request.POST)
		if form.is_valid():
			dados_form = form.data
			#cria um usuario para os dados recebidos no formulario
			usuario = User.objects.create_user(dados_form['email'], dados_form['email'],dados_form['senha'])
			#cria um perfil 
			perfil = Perfil(nome=dados_form['nome'],
							email=dados_form['email'],
							telefone=dados_form['telefone'],
							nome_empresa=dados_form['nome_empresa'],
							usuario=usuario)
			#grava o perfil no banco
			perfil.save()
			return redirect('index')

		return render(request, self.template_name, {'form' : form})