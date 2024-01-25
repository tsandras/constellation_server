from django.contrib import admin

from .models import Board, Node, Character, Background, Keystone, Notable, Skill, Spell, Speciality, Improvement

admin.site.register(Board)
admin.site.register(Node)
admin.site.register(Character)

admin.site.register(Background)
admin.site.register(Keystone)
admin.site.register(Notable)
admin.site.register(Skill)
admin.site.register(Spell)
admin.site.register(Speciality)
admin.site.register(Improvement)

# Register your models here.
