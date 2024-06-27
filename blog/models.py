from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        if len(self.title) < 5:
            raise ValidationError("El título debe tener al menos 5 caracteres.")
        if not self.content.strip():
            raise ValidationError("El contenido no puede estar vacío.")
        if not self.author.isalpha():
            raise ValidationError("El nombre del autor solo debe contener letras.")
        if len(self.author) > 100:
            raise ValidationError("El nombre del autor no debe exceder los 100 caracteres.")
