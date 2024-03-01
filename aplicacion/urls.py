from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('hardware/', hardware, name="hardware"),
    path('proyectos/', proyectos, name="proyectos"),
    path('serviciotecnico/', serviciotecnico, name="serviciotecnico"),
    path('hardwareForm/', hardwareForm, name="hardwareForm"),
    path('proyectosForm/', proyectosForm, name="proyectosForm"),
    path('serviciotecnicoForm/', serviciotecnicoForm, name="serviciotecnicoForm"),
    path('buscar/', buscar, name="buscar"),
    path('buscarHardware/', buscarHardware, name="buscarHardware"),
    path('sobremi/', sobremi, name="sobremi"),

    
    path('hardwareActualizar/<id_hardware>/', hardwareActualizar, name="hardwareActualizar"),
    path('hardwareBorrar/<id_hardware>/', hardwareBorrar, name="hardwareBorrar"),

    path('proyectosActualizar/<id_proyecto>/', proyectosActualizar, name="proyectosActualizar"),
    path('proyectosBorrar/<id_proyecto>/', proyectosBorrar, name="proyectosBorrar"),

    
    path('serviciotecnicoActualizar/<id_serviciotecnico>/', serviciotecnicoActualizar, name="serviciotecnicoActualizar"),
    path('serviciotecnicoBorrar/<id_serviciotecnico>/', serviciotecnicoBorrar, name="serviciotecnicoBorrar"),


   path('editar_perfil/', editarPerfil, name="editar_perfil"),
   path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),


    path('buscarProyecto/',buscarProyecto, name="buscarProyecto"),
    path('buscarServiciotecnico/', buscarServiciotecnico, name="buscarServiciotecnico"),
    path('login_mio/', login_mio, name="login_mio"),
    path('registrar/', registrar, name="registrar"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/home.html"), name="logout"),

]


