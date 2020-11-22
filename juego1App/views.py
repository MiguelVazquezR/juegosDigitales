from django.shortcuts import render,HttpResponse
import datetime

from juego1App.forms import FormRegistrar,FormComprar
from juego1App.models import Participante, Juego1
from sorteodj.settings import CONT_SUPER_USER

# Create your views here.
def juego1(request):
    return render(request,"juego1.html")

def comprar(request):
    if request.method == 'POST':
        form = FormComprar(request.POST)
        if form.is_valid():
            datos_form = form.cleaned_data
            if datos_form['cont_super_usuario'] == CONT_SUPER_USER:
                #crear un registro Participante 
                Participante(nombre = datos_form['nombre_completo'], juego = 'J1', contacto = datos_form['contacto'], codigo = datos_form['nombre_completo'][0:3]+str(datetime.datetime.now().strftime('%f'))).save()
                return HttpResponse('GRACIAS POR COMPRAR UN PASE. TE DESEAMOS ÉXITO')
            else:
                return HttpResponse('Error... Algo salio mal')
    else:
        form = FormComprar()
    return render(request,"juego1App/comprar.html", {"form":form})

def registrar_participante(request):#ARREGLAR EL REGISTRARVARIAS VECES CON UN SOLO CODIGO
    if request.method == 'POST':
        form = FormRegistrar(request.POST)
        if form.is_valid():
            datos_form = form.cleaned_data
            try:
                participante = Participante.objects.get(codigo=datos_form['codigo'])
            except:
                participante = False
                return HttpResponse('ERROR. El Código de participación no es válido... ')
                #Mandar mensaje de error con el codigo de participacion
            if participante:
                print(participante)
                #crear un registro de juego
                Juego1(codigo=participante.codigo, accion=datos_form['accion'], numero_accion=datos_form['num_accion']).save()
                return render(request, "registroExitoso.html", {'nombre_participante':Participante.objects.get(codigo=participante.codigo).nombre})
    else:
        form = FormRegistrar()
    return render(request,"juego1App/registrar.html", {"form":form})

def resultados(request):
    return render(request, "juego1App/resultados.html")

def participantes(request):
    lista_participantes = Participante.objects.all
    return render(request, "juego1App/participantes.html", {'lista_participantes':lista_participantes})