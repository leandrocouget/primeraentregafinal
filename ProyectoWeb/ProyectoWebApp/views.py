from django.shortcuts import render, HttpResponse
from .models import register, articles
from .forms import registroformulario, registroArticulos



# Create your views here.
def inicio(request):
   
    return render(request, "inicio.html")
    

def blog(request):
   
    return render(request, "blog.html")


def buscador(request):
   
    return render(request, "buscador.html")

def buscar(request):

    if request.GET["articulo"]:

        #respuesta = f"Estoy buscando el articulo : %r" %request.GET['articulo']
        producto = request.GET['articulo']
        articulos = articles.objects.filter(nombre__icontains=producto)
        return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto})

    else:

        respuesta = "No ingresaste articulos a buscar"
    return HttpResponse(respuesta)


def formulario(request):
    if request.method == 'POST':
        miformulario = registroformulario(request.POST)
        print(miformulario)
        if registroformulario.is_valid:
            informacion = miformulario.cleaned_data
            registro = register (nombre=informacion['nombre'], apellido=informacion['apellido'], telefono=informacion['telefono'], ciudad=informacion['ciudad'], email=informacion['email'])
            registro.save()

            return render(request, "inicio.html")

    else:
        miformulario = registroformulario()
    return render(request, "formulario.html", {"registroformulario": miformulario})


def ingreso(request):
    if request.method == 'POST':
        miformulario = registroArticulos(request.POST)
        print(miformulario)
        
        if registroArticulos.is_valid:
            informacion = miformulario.cleaned_data
            registro = articles (nombre=informacion['nombre'], precio=informacion['precio'], cantidad=informacion['cantidad'])
            registro.save()

            return render(request, "inicio.html")

    else:
        miformulario = registroArticulos()
    return render(request, "ingreso.html", {"registroArticulos": miformulario})



def contacto(request):
   
    return render(request, "contacto.html")

def base(request):
       
    return render(request, "base.html")