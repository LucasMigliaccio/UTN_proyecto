import random
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.contenttypes.models import ContentType
from .models import Categoria, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template import loader
from .forms import FormularioContacto
from django.http import Http404
from django.views.generic import View

def prueba(request):
    postsindex= Post.objects.all().order_by("fecha_publicacion")
    return render(request, "home.html", {'postsindex':postsindex})

#detalles del post
def post_detail(request, post_id):
    posts=get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post":posts})

#template privacidad
def privacidad(request):
    return render(request, "privacidad.html")

#busqueda por categoria
def postcategory(request):
    postsindex= Post.objects.all().order_by("fecha_publicacion")
    return render(request, "all_posts.html", {'postsindex':postsindex})

#busqueda por query set = categoria 
def buscar(request):
    qs= request.GET.get("category")
    
    if request.GET.get("category"):
        categoria= request.GET.get("category")
        postsindex= Post.objects.filter(categoria = Categoria.objects.get(nombre= categoria))
    else:
        postsindex= Post.objects.all().order_by("fecha_publicacion")
    return render(request, "all_posts.html", {'postsindex':postsindex})

#template sobre mi
def sobre_mi(request):
    postsindex= Post.objects.all().order_by("fecha_publicacion")
    return render(request, "about_me.html", {'postsindex':postsindex})

#form contacto
def contacto(request):
    formulario_contacto= FormularioContacto(data=request.POST)
    if formulario_contacto.is_valid():
        nombre=request.POST.get("nombre")
        email=request.POST.get("email")
        contenido=request.POST.get("contenido")
        email=EmailMessage("Mensaje desde Techmig",
        "El usuario con nombre {} con la dirección {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
        "",
        ["devmigliaccio@gmail.com"],
        reply_to=[email])
        try:
            email.send()
            return redirect("/?valido")
        except:
            return redirect("/?novalido")
    return render(request, "contact/contact.html", {"miFormulario":formulario_contacto})