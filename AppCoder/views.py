from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from AppCoder.models import Familiares

# Create your views here.

def familiares(self):

    familiares0 = Familiares(Nombre='Elena', Apellido='Ramirez', DNI=13691455, Profesion='Comerciante', FechaDeNacimineto=5/3/1961)
    familiares1 = Familiares(Nombre='Leandro', Apellido='Tolosa', DNI=39346846, Profesion='Empleado', FechaDeNacimineto=14/11/1995)
    familiares2 = Familiares(Nombre='Romina', Apellido='Melgarejo', DNI=40406776, Profesion='Abogada', FechaDeNacimineto=16/7/1997)
    familiares0.save()
    familiares1.save()
    familiares2.save()
    documentoDeTexto = f'--->Nombre: {familiares0.Nombre} Apellido: {familiares0.Apellido} DNI: {familiares0.DNI} Profesion: {familiares0.Profesion} FechaDeNacimiento: {familiares0.FechaDeNacimineto} Nombre: {familiares1.Nombre} Apellido: {familiares1.Apellido} DNI: {familiares1.DNI} Profesion: {familiares1.Profesion} FechaDeNacimiento: {familiares1.FechaDeNacimineto} Nombre: {familiares2.Nombre} Apellido: {familiares2.Apellido} DNI: {familiares2.DNI} Profesion: {familiares2.Profesion} FechaDeNacimiento: {familiares2.FechaDeNacimineto}'

    return HttpResponse(documentoDeTexto)


def nuevoTemplate(self):

    miHtml = open('C:/Users/Crist/Python310/Scripts/ProyectoCoder/AppCoder/templates/template1.html')

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)