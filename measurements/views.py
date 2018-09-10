from rest_framework import generics
from .models import Measurement
from .serializers import MeasurementSerializer


class MeasurementListCreate(generics.ListCreateAPIView):
    queryset = Measurement.objects.all().order_by('-value')[:10]
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new post."""
        serializer.save()

class MeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer