from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
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
    authentication_classes = [BasicAuthentication]
    # доступно только для авторизованных пользователей
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})
