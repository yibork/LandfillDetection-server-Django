from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Record
from .serializers import RecordSerializer

class RecordViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    @action(detail=False, methods=['delete'], url_path='delete-by-coords')
    def delete_by_coords(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')

        if not lat or not lon:
            return Response({'error': 'Latitude and longitude must be provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return Response({'error': 'Invalid latitude or longitude.'}, status=status.HTTP_400_BAD_REQUEST)

        # Find the record matching the provided latitude and longitude
        record = Record.objects.filter(lat=lat, lng=lon).first()

        if record:
            record.delete()
            return Response({'message': 'Record deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Record not found.'}, status=status.HTTP_404_NOT_FOUND)
