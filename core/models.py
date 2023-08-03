from django.db import models


class Base(models.Model):
    criado = models.DateTimeField('Data de Criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Tabela(Base):
    codigo = models.IntegerField('Código')
    descricao = models.CharField('Descrição do Produto', max_length=500)
    valor_unitario = models.DecimalField('Valor Unitário', max_digits=8, decimal_places=2)
    ativo = models.CharField('Ativo', max_length=8)
