from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer
from django.utils import timezone

@api_view(['POST'])
def register_service(request):
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        service, created = Service.objects.update_or_create(
            name=serializer.validated_data['name'],
            defaults={
                'address': serializer.validated_data['address'],
                'port': serializer.validated_data['port'],
                'last_heartbeat': timezone.now()  # Use timezone.now()
            }
        )
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK  # Use 200 OK for updates
        return Response(serializer.data, status=status_code)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def discover_service(request, name):
    try:
        service = Service.objects.get(name=name)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
    except Service.DoesNotExist:
        return Response({"detail": "Service not found."}, status=status.HTTP_404_NOT_FOUND)  # Provide a detailed message

@api_view(['DELETE'])
def deregister_service(request, name):
    try:
        service = Service.objects.get(name=name)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Service.DoesNotExist:
        return Response({"detail": "Service not found."}, status=status.HTTP_404_NOT_FOUND)  # Provide a detailed message
