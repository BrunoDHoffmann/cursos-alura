from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    OPCOES_CATEGORIAS = [
        ('NEBULOSA', 'Nebusola'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galaxia'),
        ('PLANETA', 'Planeta'),
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default='NEBULOSA')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True, null=True)
    ativo = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=datetime.now(), blank=False)
    
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"