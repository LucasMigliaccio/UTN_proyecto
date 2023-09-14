from django.urls import path
from .views import contacto, buscar, post_detail, postcategory, prueba, privacidad, sobre_mi

app_name= 'blog'

urlpatterns=[
    path("", prueba, name="bloghome"),
    path("post/<int:post_id>", post_detail, name="post_detail"),
    path("privacidad/", privacidad, name = "privacidad"),
    path("posts/", postcategory, name = "allposts"),
    path("categoria/", buscar, name = "postcategory"),
    path("about-me/", sobre_mi, name = "about-me"),
    path("contact/", contacto, name="contact"),
    ]