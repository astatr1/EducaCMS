from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from courses.models import Subject, Course
from courses.api.serializers import SubjectSerializer
from django.shortcuts import get_object_or_404


class SubjectListView(generics.ListAPIView):
    """Отдает все предметы"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """Отдает информацию по предмету"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseEnrollView(APIView):
    """Обрабатывает зачисление пользователей на курс"""
    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})
