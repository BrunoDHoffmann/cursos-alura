from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "ativo")
    list_display_links = ("nome", "id")
    search_fields = ("nome",)
    list_per_page = 10
    list_filter = ("categoria",)
    list_editable = ("ativo",)

# Register your models here.
admin.site.register(Fotografia, ListandoFotografias)