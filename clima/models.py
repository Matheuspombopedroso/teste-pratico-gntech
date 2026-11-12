from django.db import models


class Previsao(models.Model):
    cidade = models.CharField(max_length=80, default="Florianópolis")
    latitude = models.DecimalField(max_digits=9, decimal_places=4)
    longitude = models.DecimalField(max_digits=9, decimal_places=4)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    sensacao = models.DecimalField(max_digits=5, decimal_places=2)
    umidade = models.PositiveSmallIntegerField()
    vento = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=120)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.cidade} {self.temperatura}°C em {self.criado_em:%d/%m/%Y %H:%M}"