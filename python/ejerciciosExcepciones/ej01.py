#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 18 mar. 2019
Realiza un programa que pida 6 n�meros por teclado y nos diga cu�l es el
m�ximo. Si el usuario introduce un dato err�neo (algo que no sea un n�mero
entero) el programa debe indicarlo y debe pedir de nuevo el n�mero.
@author: d18momoa
'''
#Declaracion de variables
numeroPedido = 0
maximo = -99999999999999
print("Introduzca 6 numero e indicare el mayor de ellos")
#For que pide los 6 valores y en cada pasada comprueba que sea correcto, sino lo vuelve a pedir.
for x in range(0,6):
    esValido = False
    while not (esValido):
        try:
            numeroPedido = int(input("Introduzca el numero "+str(x+1)+": \n"))
            esValido = True
            if(maximo < numeroPedido):
                maximo = numeroPedido
        except:
            esValido = False
            print("Has introducido un valor incorrecto")
#Muestra el valor maximo
print("El numero mayor es: "+str(maximo))