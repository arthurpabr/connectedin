from django import forms
from django.contrib.auth.models import User
from perfis.models import Perfil

# Criando uma classe responsavel pela validacao dos dados do formulario
class RegistrarUsuarioForm(forms.Form):

	nome = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	senha = forms.CharField(required=True)
	#telefone = forms.CharField(required=True)
	#nome_empresa = forms.CharField(required=True)

	def is_valid(self):
		valid = True
		if not super(RegistrarUsuarioForm, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		user_exists = User.objects.filter(username=self.data['email']).exists()

		if user_exists:
			self.adiciona_erro('Usuario ja existente!')
			valid = False

		return valid

	def adiciona_erro(self, message):
		erros_encontrados = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		erros_encontrados.append(message)