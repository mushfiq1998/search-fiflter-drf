from .models import Student
from .serializers import StudentSerializer 
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search based on city
    search_fields = ['city']

    # search based on name or city
    # search_fields = ['name', 'city']

    # '^' starts with search
    # search_fields = ['^name']

    # '=' Exact match
    # search_fields = ['=name']

