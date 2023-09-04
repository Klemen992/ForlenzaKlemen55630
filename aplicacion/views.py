from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Plantas, Macetas, Jardineria, Decoracion, Avatar, Sustrato
from .forms import PlantasForm, MacetasForm, RegistroUsuariosForm, UserEditForm, AvatarFormulario

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")


def sobremi(request):
    return render(request, "aplicacion/aboutme.html")


# ----------------------------------------------------------------------------------------------------------------
@login_required
def plantas(request):  # contexto' es un diccionario, 'plants' es su clave
    # Plantas' es el modelo, dice que me devuelva todos los objetos de la clase o modelo Plantas
    contexto = {'plants': Plantas.objects.all(), "Titel": "disponible", "descuento": [
        "4 por 3", "20% pagando en efectivo"]}
    return render(request, "aplicacion/plants.html", contexto)


@login_required
def buscarEspecie(request):
    return render(request, "aplicacion/searchSpecies.html")


@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        plantas = Plantas.objects.filter(especie__icontains=patron)  # doble __
        contexto = {"plants": plantas,
                    'Titel': f'Especies que tienen como patron "{patron}"'}
        return render(request, "aplicacion/plants.html", contexto)

    return HttpResponse("No se ingreso nada al buscar")


# -----------------------------------------------------------------------------------------------------------------

@login_required
def macetas(request):
    # Plantas' es el modelo, dice que me devuelva todos los objetos de la clase o modelo Plantas
    contexto = {'flowerpots': Macetas.objects.all(), "Titel": "disponible", "descuento": [
        "4 por 3", "20% pagando en efectivo"]}
    return render(request, "aplicacion/flowerpots.html", contexto)


@login_required
def updateMacetas(request, id_flowerpots):
    macetas = Macetas.objects.get(id=id_flowerpots)
    if request.method == "POST":
        miForm = MacetasForm(request.POST)
        if miForm.is_valid():
            macetas.nombre = miForm.cleaned_data.get('nombre')
            macetas.material = miForm.cleaned_data.get('material')
            macetas.precio = miForm.cleaned_data.get('precio')
            macetas.save()
            # el tercero es el que desde un html llama a un url (pide la ruta) pero de macetas, no de updateMacetas, entonces es blumentoepfe
            return redirect(reverse_lazy('blumentoepfe'))

    else:
        miForm = MacetasForm(initial={
            # Use lowercase field name
            'nombre': macetas.nombre,
            'material': macetas.material,
            'precio': macetas.precio,
        })
    return render(request, "aplicacion/flowerpotsForm.html", {'form': miForm})


@login_required
def createMacetas(request):
    if request.method == "POST":
        miForm = MacetasForm(request.POST)
        if miForm.is_valid():
            m_nombre = miForm.cleaned_data.get('nombre')
            m_material = miForm.cleaned_data.get('material')
            m_precio = miForm.cleaned_data.get('precio')
            macetas = Macetas(nombre=m_nombre,
                              material=m_material,
                              precio=m_precio,
                              )
            macetas.save()
            return redirect(reverse_lazy('blumentoepfe'))
    else:
        miForm = MacetasForm()

    return render(request, "aplicacion/flowerpotsForm.html", {"form": miForm})


@login_required
def deleteMacetas(request, id_flowerpots):
    macetas = Macetas.objects.get(id=id_flowerpots)
    macetas.delete()
    return redirect(reverse_lazy('blumentoepfe'))


# --------------------------------------------------------------------------------------------------------------------

class SustratoList (LoginRequiredMixin, ListView):
    model = Sustrato


class SustratoCreate(LoginRequiredMixin, CreateView):
    model = Sustrato
    fields = ['nombre', 'tamanio', 'precio']
    success_url = reverse_lazy('substrat')


class SustratoUpdate(LoginRequiredMixin, UpdateView):
    model = Sustrato
    fields = ['nombre', 'tamanio', 'precio']
    success_url = reverse_lazy('substrat')


class SustratoDelete(LoginRequiredMixin, DeleteView):
    model = Sustrato
    success_url = reverse_lazy('substrat')


# ----------------------------------------------------------------------------------------------------------
class JardineriaList (LoginRequiredMixin, ListView):
    model = Jardineria


class JardineriaCreate(LoginRequiredMixin, CreateView):
    model = Jardineria
    fields = ['nombre', 'tipo', 'precio']
    success_url = reverse_lazy('garten')


class JardineriaUpdate(LoginRequiredMixin, UpdateView):
    model = Jardineria
    fields = ['nombre', 'tipo', 'precio']
    success_url = reverse_lazy('garten')


class JardineriaDelete(LoginRequiredMixin, DeleteView):
    model = Jardineria
    success_url = reverse_lazy('garten')


# ----------------------------------------------------------------------------------------------------------------


class DecoracionList (LoginRequiredMixin, ListView):
    model = Decoracion


class DecoracionCreate(LoginRequiredMixin, CreateView):
    model = Decoracion
    fields = ['nombre', 'tipo', 'precio']
    success_url = reverse_lazy('dekoration')


class DecoracionUpdate(LoginRequiredMixin, UpdateView):
    model = Decoracion
    fields = ['nombre', 'tipo', 'precio']
    success_url = reverse_lazy('dekoration')


class DecoracionDelete(LoginRequiredMixin, DeleteView):
    model = Decoracion
    success_url = reverse_lazy('dekoration')


# ------------------------------------------------------------------------------------------------------------------


def login_request(request):
    if request.method == "POST":
        # request, este formulario es el que recarga lo que pusimos en la base.html
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(
                        user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a nuestro vivero virtual {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm})


def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = RegistroUsuariosForm()
    return render(request, "aplicacion/registro.html", {"form": miForm})


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html")
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        # Diferente a los forms tradicionales
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})


# FUNCION QUE NOS PERMITA DAR DE ALTA NUESTRO AVATAR
