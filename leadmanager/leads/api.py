from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

#Load ViewSet
class LeadViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()