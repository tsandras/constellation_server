from django.http import HttpResponse
from rest_framework import viewsets
from characters.serializers import BoardSerializer
from characters.models import Board

# class BoardViewSet(viewsets.mixins.RetrieveModelMixin, viewsets.mixins.ListModelMixin):
class BoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows boards to be listed and retrieved.
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the characters index.")
