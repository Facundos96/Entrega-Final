from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *


from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login

from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def proyectos (request):
    contexto = {'proyectos': Proyectos.objects.all()}
    return render(request,"aplicacion/proyectos.html",contexto)


def hardware (request):
    contexto = {'hardware': Hardware.objects.all()}
    return render(request,"aplicacion/hardware.html",contexto)


def serviciotecnico(request):
    contexto = {'serviciotecnico': Serviciotecnico.objects.all()}
    return render(request,"aplicacion/serviciotecnico.html",contexto)
                  
def sobremi(request):
   return render(request,"aplicacion/sobremi.html")
    
@login_required
def hardwareForm(request):
    if request.method == "POST":
        miForm = HardwareForms(request.POST)
        if miForm.is_valid():
            hardware_nombre = miForm.cleaned_data.get("nombre")
            hardware_tipo = miForm.cleaned_data.get("tipo")
            hardware_precio=miForm.cleaned_data.get("precio")
            harware = Hardware(nombre=hardware_nombre, tipo=hardware_tipo,precio=hardware_precio)
            harware.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = HardwareForms()

    return render(request, "aplicacion/hardwareForm.html", {"form": miForm })

@login_required
def proyectosForm(request):
    if request.method == "POST":
        miForm = ProyectosForm(request.POST)
        if miForm.is_valid():
            proyecto_nombre = miForm.cleaned_data.get("nombre")
            proyecto_lenguaje = miForm.cleaned_data.get("lenguaje")
            proyecto_horas=miForm.cleaned_data.get("horas")
            proyecto_estado=miForm.cleaned_data.get("estado")
            proyecto_descripcion=miForm.cleaned_data.get("descripcion")
            proyecto = Proyectos(nombre=proyecto_nombre, lenguaje=proyecto_lenguaje ,horas=proyecto_horas,estado=proyecto_estado,descripcion=proyecto_descripcion)
            proyecto.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = ProyectosForm()

    return render(request, "aplicacion/proyectosForms.html", {"form": miForm })

@login_required
def hardwareActualizar(request, id_hardware):
    hardware = Hardware.objects.get(id=id_hardware)
    if request.method == "POST":
        miForm = HardwareForms(request.POST)
        if miForm.is_valid():
            hardware.nombre = miForm.cleaned_data.get("nombre")
            hardware.tipo = miForm.cleaned_data.get("tipo")
            hardware.precio=miForm.cleaned_data.get("precio")
            hardware.save()
        return redirect(reverse_lazy('hardware'))   

    else:    
        miForm = HardwareForms(initial={
            'nombre': hardware.nombre,
            'tipo': hardware.tipo,
            'precio': hardware.precio,
           
        })
    return render(request, "aplicacion/hardwareForm.html", {'form': miForm})
@login_required
def serviciotecnicoActualizar(request, id_serviciotecnico):
    serviciotecnico = Serviciotecnico.objects.get(id=id_serviciotecnico)
    if request.method == "POST":
        miForm = ServiciotecnicoForm(request.POST)
        if miForm.is_valid():
            serviciotecnico.nombre = miForm.cleaned_data.get("nombre")
            serviciotecnico.estado=miForm.cleaned_data.get("estado")
            serviciotecnico.precio=miForm.cleaned_data.get("precio")
            serviciotecnico.descripcion=miForm.cleaned_data.get("descripcion")
            serviciotecnico.save()
            return redirect(reverse_lazy('serviciotecnico')) 

    else:    
        miForm = ServiciotecnicoForm(initial={
            'nombre': serviciotecnico.nombre,
            'estado': serviciotecnico.estado,
            'precio': serviciotecnico.precio,
           'descripcion':serviciotecnico.descripcion
        })
    return render(request, "aplicacion/serviciotecnicoForm.html", {'form': miForm})

@login_required
def proyectosActualizar(request, id_proyecto):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    if request.method == "POST":
        miForm = ProyectosForm(request.POST)
        if miForm.is_valid():
            proyecto.nombre = miForm.cleaned_data.get("nombre")
            proyecto.lenguaje = miForm.cleaned_data.get("lenguaje")
            proyecto.horas=miForm.cleaned_data.get("horas")
            proyecto.estado=miForm.cleaned_data.get("estado")
            proyecto.descripcion=miForm.cleaned_data.get("descripcion")
            proyecto.save()
        return redirect(reverse_lazy('proyectos'))   

    else:    
        miForm = ProyectosForm(initial={
            
            'nombre': proyecto.nombre,
            'lenguaje': proyecto.lenguaje,
            'horas': proyecto.horas,
            'estado': proyecto.estado,
            'descripcion': proyecto.descripcion,
           
        })
    return render(request, "aplicacion/proyectosForms.html", {'form': miForm})

@login_required
def hardwareBorrar(request, id_hardware):
    hardware = Hardware.objects.get(id=id_hardware)
    hardware.delete()
    return redirect(reverse_lazy('hardware'))





@login_required
def serviciotecnicoBorrar(request, id_serviciotecnico):
    serviciotecnico = Serviciotecnico.objects.get(id=id_serviciotecnico)
    serviciotecnico.delete()
    return redirect(reverse_lazy('serviciotecnico'))







@login_required
def proyectosBorrar(request, id_proyecto):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    proyecto.delete()
    return redirect(reverse_lazy('proyectos'))



@login_required
def serviciotecnicoForm(request):
    if request.method == "POST":
        miForm = ServiciotecnicoForm(request.POST)
        if miForm.is_valid():
            serviciotecnico_nombre = miForm.cleaned_data.get("nombre")
            serviciotecnico_estado=miForm.cleaned_data.get("estado")
            serviciotecnico__precio=miForm.cleaned_data.get("precio")
            serviciotecnico_descripcion=miForm.cleaned_data.get("descripcion")
            serviciotecnico = Serviciotecnico(nombre=serviciotecnico_nombre, precio=serviciotecnico__precio ,estado=serviciotecnico_estado,descripcion=serviciotecnico_descripcion)
            serviciotecnico.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = ServiciotecnicoForm()

    return render(request, "aplicacion/serviciotecnicoForm.html", {"form": miForm })



def buscar(request):
    return render(request, "aplicacion/buscar.html")

def buscarHardware(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        hardware = Hardware.objects.filter(nombre__icontains=patron)
        contexto = {"hardware": hardware }
        return render(request, "aplicacion/hardware.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")




def buscarProyecto(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        proyectos = Proyectos.objects.filter(nombre__icontains=patron)
        contexto = {"proyectos": proyectos }
        return render(request, "aplicacion/proyectos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

def buscarServiciotecnico(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        serviciotecnico = Serviciotecnico.objects.filter(nombre__icontains=patron)
        contexto = {"serviciotecnico": serviciotecnico }
        return render(request, "aplicacion/serviciotecnico.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")


def login_mio(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)

            #____ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #__________________________________________

            return render(request, "aplicacion/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login_mio.html", {"form": miForm })    

def registrar(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "aplicacion/registrar.html", {"form": miForm })  


def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": form }) 

def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # __________________________________
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___________ Hago una url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/home.html")

    else:    
        form = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": form })     