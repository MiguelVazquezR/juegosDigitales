from django.contrib import admin
from .models import Participante, Juego1

# Register your models here.

class ParticipanteAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','codigo')

class Juego1Admin(admin.ModelAdmin):
    readonly_fields = ('creado','codigo')

admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Juego1, Juego1Admin)