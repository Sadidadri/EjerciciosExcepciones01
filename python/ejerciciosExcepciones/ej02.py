#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 18 mar. 2019
Modifica la clase Gato vista anteriormente a�adiendo el m�todo apareaCon.
Este m�todo debe comprobar que los gatos son de distinto sexo, tras lo
cual, genera un nuevo gato. Por ejemplo, ser�a v�lido algo como Gato cria
= garfield.apareaCon(lisa). En caso de que los gatos sean del mismo sexo,
el m�todo debe generar la excepci�n ExcepcionApareamientoImposible. Crea un
programa desde el que se pruebe el m�todo.
@author: d18momoa
'''
from ejerciciosExcepciones.gatoSimple2 import GatoSimple2
#Creamos 4 gatos, 2 hembras y 2 machos
garfield = GatoSimple2("macho")
lisa = GatoSimple2("hembra")

tom = GatoSimple2("macho")
ariel = GatoSimple2("hembra")

try:
    #En esta linea podemos comprobar que se produce correctamente
    garfield.apareaCon(lisa)
    #Aqui lanza la excepcion
    #garfield.apareaCon(tom)
except:
    print("Excepcion capturada con exito")