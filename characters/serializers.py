# from django.contrib.auth.models import Group, User
from characters.models import Board, Node
from rest_framework import serializers

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = [
            "id", "name", "description", "position_x", "position_y",
            "category", "bonus", "bonus_range", "skill", "spell",
            "notable", "keystone", "skill_expertise", "spell_expertise",
            "links"
        ]

class BoardSerializer(serializers.ModelSerializer):

    nodes = NodeSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'name', 'description', 'nodes']