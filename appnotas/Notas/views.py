from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime
from .forms import NotaForm
from .models import Nota 

# Vista principal de notas
def NotasIndex(request):
    #consultar notas 
    Notas = Nota.objects.all()
   

    #Consultar productos
    Nota_list = Nota.objects.all()
    #Configurar paginación cada 9 notas
    paginator = Paginator(Nota_list, 9)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)
    #Obtener el template
    template = loader.get_template("Notas.html")
    #Agregar el contexto
    context = {"page_obj": page_obj,"Notas":Notas}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un autor
def detalleNotas(request, id):
    #Consultar notas
    Notas = Nota.objects.get(id=id)           
    #Consultar datos de Notas
    context = {'Nota':Notas}
    #Obtener el template
    template = loader.get_template("detalleNotas.html")

    return HttpResponse(template.render(context,request))

# Vista principal de Gestión de Notas
def gestionNotas(request):
    
    # Consultar Notas y ordenar por fecha de más nueva a más vieja
    
    Nota_list = Nota.objects.all().order_by('fecha','id')
    
    # Configurar paginación cada 10 Notas
    paginator = Paginator(Nota_list, 10)

    # Obtener página
    page_number = request.GET.get('page', 0)
    page_obj = paginator.get_page(page_number)

    # Obtener el template
    template = loader.get_template("gestionNotas.html")

    # Agregar el contexto
    context = {"page_obj": page_obj}

    # Retornar respuesta http
    return HttpResponse(template.render(context, request))

# Vista para crear Notas
def crearNotas(request):
    #Obtener el template
    template = loader.get_template("crearNotas.html")
    #Generar Formulario
    if request.method == "POST":
        form = NotaForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            producto_nuevo = form.save(commit=False)
            #Asignar fecha de creación
            producto_nuevo.fecha_creacion = datetime.now()
            #Guardar Nota
            producto_nuevo.save()
            return redirect('gestionNotas')
    else:
        form = NotaForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista de Notas
def editarNotas(request,id):
    #Obtener el template
    template = loader.get_template("editarNota.html")
    #Buscar Nota
    obj = get_object_or_404(Nota, id = id)
    #formulario que contiene la instancia
    form = NotaForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('gestionNotas')   
    #Agregar el contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista de Nota
def eliminarNotas(request,id):
    #Obtener el template
    template = loader.get_template("eliminarNota.html")
    #Buscar la Nota
    obj = get_object_or_404(Nota, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('gestionNotas')
    #Agregar el contexto
    context = {}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))
   

def verNotas(request, nota_id):  # Debe coincidir con el nombre en la URL
    nota = get_object_or_404(Nota, id=nota_id)
    return render(request, 'verNotas.html', {'nota': nota})