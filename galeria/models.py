from django.db import models

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
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"