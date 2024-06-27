from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    # Validación de longitud del título
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El título debe tener al menos 5 caracteres.")
        return value

    # Validación de contenido no vacío
    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("El contenido no puede estar vacío.")
        return value

    # Validación del autor
    def validate_author(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("El nombre del autor solo debe contener letras.")
        if len(value) > 100:
            raise serializers.ValidationError("El nombre del autor no debe exceder los 100 caracteres.")
        return value
