from rest_framework import serializers
from projects.models import Project

class Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'