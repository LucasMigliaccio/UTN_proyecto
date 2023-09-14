from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.urls import reverse




#modelo base para heredar
class ModeloBase(models.Model):
    id=models.AutoField(primary_key=True)
    estado= models.BooleanField('Estado', default=True)
    fecha_creacion=models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    fecha_modificacion=models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    fecha_eliminacion=models.DateField('Fecha de eliminación', auto_now=True, auto_now_add=False)  


    class Meta:
        abstract= True #la clase abstracta permite no mandar esto a la db, sino que agregarlas donde lo requiramos


#modelo de categoria
class Categoria(ModeloBase):
    nombre= models.CharField('Nombre de la Categoria', max_length=100, unique=True)
    imagen_referencial=models.ImageField('Imagen Referencial', upload_to='categoria/images/')

    class Meta:
        verbose_name= "Categoria"
        verbose_name_plural= "Categorias"

    def __str__(self):
        return self.nombre

#modelo de autor
class Autor(ModeloBase):
    nombre= models.CharField("Nombres", max_length=100)
    apellidos=models.CharField("Apellidos", max_length=120)
    email=models.EmailField("Correo Electrónico", max_length=150)
    descripcion=models.TextField("Descripción")
    web=models.URLField("Web", null=True, blank=True)
    linkedin=models.URLField("LinkedIn", null=True, blank=True)
    github=models.URLField("GitHub", null=True, blank=True)
    img = models.ImageField('Imagen Referencial', null = True, blank = True,upload_to = 'blog/images/autores/')

    class Meta:
        verbose_name= "Autor"
        verbose_name_plural= "Autores"

    def __str__(self):
        return "{1} {0}".format(self.apellidos,self.nombre)

#modelo de posts
class Post(ModeloBase):
    titulo=models.CharField("Titulo del Post", max_length=150, unique=True)
    slug=models.CharField("Slug", max_length=150, unique=True)
    descripcion=models.TextField("Descripción")
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    contenido=RichTextField()
    img=models.ImageField(upload_to="blog/images/", max_length=255)
    publicado= models.BooleanField("Publicado/No Publicado", default=False)
    fecha_publicacion= models.DateField("Fecha publcación")


    class Meta:
        verbose_name= "Post"
        verbose_name_plural= "Posts"

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return f"/post/{self.titulo}/"


class Web(ModeloBase):
    nosotros=models.TextField("Nosotros")
    email=models.EmailField("Correo Electrónico", max_length=150)

    class Meta:
        verbose_name= "Web"
        verbose_name_plural= "Webs"

    def __str__(self):
        return self.nosotros


class RedesSociales(ModeloBase):
    instagram=models.URLField("Instagram")
    linkedin=models.URLField("LinkedIn", null=True, blank=True)
    stackoverflow=models.URLField("Stackoverflow", null=True, blank=True)


    class Meta:
        verbose_name="Red Social"
        verbose_name_plural="Redes Sociales"

    def __str__(self):
        return self.linkedin


#########
#modelo de contacto
class Contacto(ModeloBase):
    nombre= models.CharField("Nombre", max_length=150)
    apellido=models.CharField("Apellido", max_length=150)
    correo=models.EmailField("Correo Electrónico", max_length=150)
    asunto=models.CharField("Asunto", max_length=200)
    mensaje=models.TextField("Mensaje")

    class Meta:
        verbose_name= "Contacto"
        verbose_name_plural= "Contactos"

    def __str__(self):
        return self.asunto

#modelo de subscriptor
class Subscriptor(ModeloBase):
    correo=models.EmailField("Correo Electrónico", max_length=150)
    
    class Meta:
        verbose_name= "Subscriptor"
        verbose_name_plural= "Subscriptores"
    
    def __str__(self):
        return self.correo
