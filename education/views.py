from rest_framework import generics
from .models import EducationalContent
from .serializers import EducationalContentSerializer

class EducationalContentListCreateView(generics.ListCreateAPIView):
    queryset = EducationalContent.objects.all()
    serializer_class = EducationalContentSerializer