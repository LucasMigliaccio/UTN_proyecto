from rest_framework import viewsets
from .models import ProjectRestApi
from .serializer import ProjectBlogRestApiSerializer

class ProjectBlogViewSet(viewsets.ModelViewSet):
    queryset= ProjectRestApi.objects.all()
    serializer_class= ProjectBlogRestApiSerializer