from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Teacher, Category, Student
from .serializers import CategorySerializer, TeacherSerializer, StudentSerializer

class CategoryList(generics.ListAPIView): # GET
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView): # POST
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveView(generics.RetrieveAPIView): # GET 1 категория
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateView(generics.UpdateAPIView): # PUT/PATCH
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView): # GET/POST
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


#viewsets

class CategoryListCreateUpdateDeleteView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]