
from rest_framework import serializers
from projects.models import Project
import datetime
class Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'
    def validate_deadline(self,value):
        today=datetime.date.today()
        if value <= today:
            raise serializers.ValidationError('Deadline must be in the future.')
        return value