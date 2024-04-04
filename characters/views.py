from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from characters.serializers import BoardSerializer
from characters.models import Board

class BoardViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows boards to be listed and retrieved.
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
