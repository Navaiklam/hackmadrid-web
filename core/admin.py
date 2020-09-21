from django.contrib import admin
from .models import TipoEvento, Event
 
class EventosAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_filter = ['tipoevento']
    search_fields = ['ponente','nombre']
    list_display = ['nombre','ponente','duracion','anio','tipoevento','img']
    
# Register your models here.
admin.site.register(TipoEvento)
admin.site.register(Event, EventosAdmin)

