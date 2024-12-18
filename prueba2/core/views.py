from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioForm, LibroForm, ReviewForm

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Usuario registrado exitosamente!")
            return redirect('registro_exitoso')  # Redirigir a página de éxito
        else:
            messages.error(request, "Hubo errores en el formulario. Verifica los campos.")
    else:
        form = UsuarioForm()
    return render(request, 'registro_usuario.html', {'form': form})

def registro_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Libro registrado exitosamente!")
            return redirect('registro_exitoso_libro')  # Redirigir a página de éxito
        else:
            messages.error(request, "Hubo errores en el formulario. Verifica los campos.")
    else:
        form = LibroForm()
    return render(request, 'registro_libro.html', {'form': form})

def registro_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Reseña registrada exitosamente!")
            return redirect('registro_exitoso_review')  # Redirigir a página de éxito
        else:
            messages.error(request, "Hubo errores en el formulario. Verifica los campos.")
    else:
        form = ReviewForm()
    return render(request, 'registro_review.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')

def registro_exitoso_libro(request):
    return render(request, 'registro_exitoso_libro.html')

def registro_exitoso_review(request):
    return render(request, 'registro_exitoso_review.html')
