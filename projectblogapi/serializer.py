from .models import ProjectRestApi
from  rest_framework import serializers



class ProjectBlogRestApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRestApi
        fields= '__all__'