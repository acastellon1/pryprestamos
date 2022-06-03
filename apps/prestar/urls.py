from django.urls import path

from apps.prestar.views import consulta1, consulta2, consulta3, ejemplarCreate, ejemplarEdit, ejemplarElim, listEjemplar, listUsuario, listprestar, prestarCreate, prestarEdit, prestarElim, usuarioCreate, usuarioEdit, usuarioElim

app_name= 'prestar'
urlpatterns = [
    path('', listprestar, name = 'listprestar'),
    path('nuevop/', prestarCreate, name = 'prestarCreate'),
    path('actualizarp/<int:id_prestar>/', prestarEdit, name='prestarEdit'),
    path('eliminarp/<int:id_prestar>/', prestarElim, name='prestarElim'),

    ######### Usuario ############

    path('usuarios', listUsuario, name = 'listUsuario'),
    path('nuevou/', usuarioCreate, name = 'usuarioCreate'),
    path('actualizaru/<int:id_usuario>/', usuarioEdit, name='usuarioEdit'),
    path('eliminaru/<int:id_usuario>/', usuarioElim, name='usuarioElim'),

    ######### Ejemplar #############

    path('ejemplares', listEjemplar, name = 'listEjemplar'),
    path('nuevoe/', ejemplarCreate, name = 'ejemplarCreate'),
    path('actualizare/<int:id_ejemplar>/', ejemplarEdit, name='ejemplarEdit'),
    path('eliminare/<int:id_ejemplar>/', ejemplarElim, name='ejemplarElim'),


############ Consultas ###############
    path('consulta1', consulta1, name = 'consulta1'),
    path('consulta2', consulta2, name = 'consulta2'),
    path('consulta3', consulta3, name = 'consulta3'),




]