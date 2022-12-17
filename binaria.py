#!/usr/bin/python3
#
# File:     binaria.py
# Created:  17.06.2020
#

def ricerca_binaria(dato, lista):
	a = 0
	b = len(lista)
	risultato = -1
	m = a
	controllo = b
	while controllo != m and risultato < 0:
		controllo = m
		m = int((a+b)/2)
		if dato == lista[m]: risultato = m
		elif dato > lista[m]: a = m
		else: b = m
	return risultato
	
lista = [10, 20, 30, 40, 50, 60, 70]
dato = int(input('Introduci un numero '))
risultato = ricerca_binaria(dato, lista)
if risultato < 0: print('Non trovato')
else: print('Trovato in posizione ', risultato)