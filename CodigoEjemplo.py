#Clase que refleja las vistas de un proyecto en DJANGO
from django.shortcuts import render, redirect
from .models import Categoria, Videojuego
from .form_categoria import CategoriaForm
from .form_videojuego import VideojuegoForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Count
from django_weasyprint import WeasyTemplateResponseMixin
from django.conf import settings

#from django views.generic import ListView
# Create your views here.

def lista_categoria(request):
    #categorias es igual al modelo categorias
    #Practicamente se hace un select * from categorias
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def eliminar_categoria(request, id):
    #busca en categoria el id
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('categoriaapp:lista')
    

def nuevo_categoria(request):
    form = CategoriaForm()

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoriaapp:lista')
    context = {'form': form }
    return render(request, 'nuevo_categoria.html', context)

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = CategoriaForm(instance=categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoriaapp:lista')
    context = {'form': form }
    return render(request, 'editar_categoria.html', context)

'''
#Excepciones controladas
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(instance=categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')
    context = {'form': form }
    return render(request, 'editar_categoria.html', context)
'''

def listavj(request):
    titvideojuego = Videojuego.objects.all()
    return render(request, 'lista_tvideojuegos.html',{'titvideojuego': titvideojuego})

def eliminarvj(request, id):
    titulov = Videojuego.objects.get(id=id)
    titulov.delete()
    return redirect('videojuego:listavj')

def nuevo_vj(request):
    form = VideojuegoForm()

    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videojuegoapp:listavj')
    context = {'form': form }
    return render(request, 'nuevo_videojuego.html', context)

def editar_vj(request, id):
    videoj = Videojuego.objects.get(id=id)
    form = VideojuegoForm(instance=videoj)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, instance=videoj)
        if form.is_valid():
            form.save()
            return redirect('videojuegoapp:listavj')
    context = {'form': form }
    return render(request, 'editar_videojuego.html', context)



class VideojuegoList(ListView):
    model = Videojuego 
    # context_object_name = 'videojuegos'
    # extra_context = {
    #     'var1': 'Clases génericas',
    #     'nombre': 'Yere',
    # }
    # queryset = Videojuego.objects.filter(anio=1997)

class VideojuegoEliminar(DeleteView):
    model = Videojuego
    success_url = reverse_lazy('videojuegoapp:listaBC')

class VideojuegoCrear(CreateView):
    model = Videojuego
    #fields = '__all__'
    form_class = VideojuegoForm
    extra_context = {'etiqueta': 'Nuevo','boton': 'Agregar', 'vj_nuevo': True}
    success_url = reverse_lazy('videojuegoapp:listaBC')

class VideojuegoActualizar(UpdateView):
    model = Videojuego
    form_class = VideojuegoForm
   # fields = '__all__'
    #Diccionario de 
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    success_url = reverse_lazy('videojuegoapp:listaBC')

class VideojuegoDetalle(DetailView):
    model = Videojuego



###########################

class CategoriaList(ListView):
    paginate_by=5
    model = Categoria 

class CategoriaEliminar(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoriaapp:listaBC')

class CategoriaCrear(CreateView):
    model = Categoria
    fields = '__all__'
    extra_context = {'etiqueta': 'Nuevo','boton': 'Agregar'}
    success_url = reverse_lazy('categoriaapp:listaBC')

class CategoriaActualizar(UpdateView):
    model = Categoria
    fields = '__all__'
    #Diccionario de 
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    success_url = reverse_lazy('categoriaapp:listaBC')

class CategoriaDetalle(DetailView):
    model = Categoria


class Grafica(TemplateView):
    template_name = 'videojuego/grafica.html'
    
    def get(self, request, *args, **kwargs):
        videojuegos = Videojuego.objects.all().values('categoria').annotate(cuantos=Count('categoria'))
        categorias = Categoria.objects.all()
    
        datos = []
        for categoria in categorias:
            cuantos = 0
            for dp in videojuegos: 
                if dp['categoria'] == categoria.id:
                    cuantos = dp['cuantos']
                    break
            datos.append({'name':categoria.nombre, 'data':[cuantos]})
    
        self.extra_context = {'datos': datos}
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class VistaPdf(ListView):
    model= Videojuego
    template_name='videojuego/videojuegopdf.html'

class ListaVideojuegodPdf(WeasyTemplateResponseMixin, VistaPdf):
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'css/bootstrap.min.css',
    ]
    pdf_attachment = False
    pdf_filename='ListaVideojuegos.pdf'

class Vista2Pdf(DetailView):
    model= Videojuego
    template_name='videojuego/repvideojuegopdf.html'

class ReporteVideojuegoPdf(WeasyTemplateResponseMixin, Vista2Pdf):
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'css/bootstrap.min.css',
    ]
    pdf_attachment = False
    pdf_filename='Videojuego.pdf'

#sudo apt-get install libpangocairo-1.0-0