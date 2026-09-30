from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Teacher, Category, Student
from .serializers import CategorySerializer, TeacherSerializer, StudentSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer