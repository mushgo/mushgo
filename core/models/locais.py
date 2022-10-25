from unittest.util import _MAX_LENGTH
from django.db import models

class Local(models.Model):
    nome = models.CharField(max_length=45)
    

    def __str__(self):
        return self.nome

