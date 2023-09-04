from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name="home"),
    path('aboutme', sobremi, name="uebermich"),


    path('plants/', plantas, name="pflanzen"),
    path('searchSpecies/', buscarEspecie, name="suchen_gattung"),
    path('search2/', buscar2, name="suchen_2"),

    path('flowerpots/', macetas, name="blumentoepfe"),
    path('update_flowerpots/<id_flowerpots>/',
         updateMacetas, name="update_blumentoepfe"),
    path('delete_flowerpots/<id_flowerpots>/',
         deleteMacetas, name="delete_blumentoepfe"),
    path('create_flowerpot/', createMacetas, name="create_blumentoepfe"),



    path('decoration/', DecoracionList.as_view(), name="dekoration"),
    path('create_decoration/', DecoracionCreate.as_view(),
         name="create_dekoration"),
    path('update_decoration/<int:pk>/',
         DecoracionUpdate.as_view(), name="update_dekoration"),
    path('delete_decoration/<int:pk>/',
         DecoracionDelete.as_view(), name="delete_dekoration"),


    path('substratum/', SustratoList.as_view(), name="substrat"),
    path('create_substratum/', SustratoCreate.as_view(),
         name="create_substrat"),
    path('update_substratum/<int:pk>/',
         SustratoUpdate.as_view(), name="update_substrat"),
    path('delete_substratum/<int:pk>/',
         SustratoDelete.as_view(), name="delete_substrat"),


    # path('gardering/',jardineria, name="garten"),
    path('gardering/', JardineriaList.as_view(), name="garten"),
    path('create_gardering/', JardineriaCreate.as_view(), name="create_garten"),
    path('update_gardering/<int:pk>/',
         JardineriaUpdate.as_view(), name="update_garten"),
    path('delete_gardering/<int:pk>/',
         JardineriaDelete.as_view(), name="delete_garten"),


    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registro/', register, name="registro"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]
