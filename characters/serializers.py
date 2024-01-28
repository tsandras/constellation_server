# from django.contrib.auth.models import Group, User
from characters.models import Board, Node, Skill
from rest_framework import serializers

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id", "name", "description", "category"
        ]

class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id", "name", "description", "category"
        ]

class NodeSerializer(serializers.ModelSerializer):

    skill = SkillSerializer(read_only=True)
    spell = SpellSerializer(read_only=True)

    class Meta:
        model = Node
        fields = [
            "id", "name", "description", "position_x", "position_y",
            "category", "bonus", "bonus_range", "skill", "spell",
            "notable", "keystone", "skill_expertise", "spell_expertise",
            "links", "image_name"
        ]

class BoardSerializer(serializers.ModelSerializer):

    nodes = NodeSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'name', 'description', 'nodes']