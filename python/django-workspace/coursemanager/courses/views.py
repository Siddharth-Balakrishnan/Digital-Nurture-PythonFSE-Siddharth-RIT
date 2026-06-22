from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Student, Enrollment
from .serializers import CourseSerializer, StudentSerializer, EnrollmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """Automatically provides list, create, retrieve, update, and destroy actions."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Custom action to get students for a specific course
    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        course = self.get_object() # Gets the specific course
        # Find enrollments for this course, then get the students
        enrollments = Enrollment.objects.filter(course=course).select_related('student')
        students = [enrollment.student for enrollment in enrollments]
        
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer