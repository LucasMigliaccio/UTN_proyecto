from django.shortcuts import redirect, render
from django.views.generic import View
from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
class VRegistro(View):

    def get(self, request):

        formulario= UserCreationForm()
        return render(request, "register.html", {"form":formulario}) 

    def post(self, request):

        formulario=UserCreationForm(request.POST)
        if formulario.is_valid():

            usuario= formulario.save()
            login(request, usuario)
            return redirect('blog:bloghome')
        
        else:
            for msg in formulario.error_messages:
                messages.error(request, formulario.error_messages[msg])
            
            return render(request, "register.html", {"form":formulario}) 

def cerrar_sesion(request):
    
    logout(request)
    return redirect('blog:bloghome')

def logeo(request):

    if request.method == 'POST':
        formulario= AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_usuario=formulario.cleaned_data.get("username")
            contra=formulario.cleaned_data.get("password")
            usuario= authenticate(username= nombre_usuario, password= contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('blog:bloghome')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")


    formulario= AuthenticationForm()
    return render(request, "login.html", {"form":formulario})