from django import forms
from .models import Usuario, Libro, Review
import re

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()  # Establecer el widget PasswordInput aquí
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("El email debe terminar en @example.com")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r'[0-9]', password):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        if not all(cleaned_data.values()):  # Verificar que todos los campos están llenos
            raise forms.ValidationError("Todos los campos son obligatorios.")
        return cleaned_data

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['title', 'author', 'genre', 'published_date', 'isbn']

    def clean(self):
        cleaned_data = super().clean()
        if not all(cleaned_data.values()):
            raise forms.ValidationError("Todos los campos son obligatorios.")
        return cleaned_data

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'book', 'rating', 'comment']

    def clean(self):
        cleaned_data = super().clean()
        if not all(cleaned_data.values()):
            raise forms.ValidationError("Todos los campos son obligatorios.")
        return cleaned_data
