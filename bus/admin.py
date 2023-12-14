from django.contrib.admin import ModelAdmin, register
from .models import Terminal, Buses


@register(Terminal)
class TerminalAdmin(ModelAdmin):
    pass


@register(Buses)
class BusesAdmin(ModelAdmin):
    pass
