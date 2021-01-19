from django.contrib import admin

from .models import Area, Prioridad, Estado, Aviso, Nota

class AreaAdmin(admin.ModelAdmin):
  list_display = ('area', 'descripcion','estatus')
admin.site.register(Area, AreaAdmin)

class PrioridadAdmin(admin.ModelAdmin):
  list_display = ('prioridad','orden')
admin.site.register(Prioridad, PrioridadAdmin)

admin.site.register(Estado)
admin.site.register(Aviso)
admin.site.register(Nota)


