from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from django.core.paginator import Paginator

# Create your views here.

def crearlibros(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        publicado = request.POST.get('publicado')
        genero = request.POST.get('genero')  
        Libro.objects.create(titulo=titulo, autor=autor, publicado=publicado, genero=genero)
        return redirect('listar_libros')
    return render(request, 'crearlibro.html')

def listarlibros(request):
    libros = Libro.objects.select_related('usuario').filter(usuario=request.user)
    paginator = Paginator(libros, 5) #5 libros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'listarlibros.hmtl', {'libros': libros}, {'page_obj':page_obj})


