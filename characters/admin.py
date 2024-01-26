from django.contrib import admin

from .models import Board, Node, Character, Background, Keystone, Notable, Skill, Spell, Speciality, Improvement

admin.site.register(Character)

admin.site.register(Background)
admin.site.register(Keystone)
admin.site.register(Notable)
admin.site.register(Skill)
admin.site.register(Spell)
admin.site.register(Speciality)
admin.site.register(Improvement)

class NodeAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
         print(kwargs)
         if 'obj' in kwargs and kwargs['obj'] is not None:
            context['adminform'].form.fields['links'].queryset = Node.objects.filter(board_id=kwargs['obj'].board_id)
         return super(NodeAdmin, self).render_change_form(request, context, *args, **kwargs)
    
    list_display = ["id", "name", "board", "category"]
    list_display_links = ['id', 'name']

admin.site.register(Node, NodeAdmin)

class BoardAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ['id', 'name']

admin.site.register(Board, BoardAdmin)