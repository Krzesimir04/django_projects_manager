from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Project_Serializer
from projects.models import Project
# Create your views here.
@api_view(['GET'])
def get_data(request):
    projects=Project.objects.all()
    serializer=Project_Serializer(projects,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_data(request,pk):
    project=Project.objects.get(id=pk)
    serializer=Project_Serializer(instance=project,data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['PUT'])
def put_data(request):
    serializer=Project_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_data(request,pk):
    Project.objects.filter(id=pk).delete()
    return Response('Item deleted')