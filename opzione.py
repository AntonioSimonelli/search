#!/usr/bin/python3
#
# File:     opzione.py
# Created:  17.06.2020
# Author:   Antonio Simonelli <a.simonelli@tin.it>
# Copyright (c) 2014-2020
# License:  GNU LGPL Version 3, 2007
#

def opzione_laterale(dato, x):
	risultato = -1
	n = len(x)
	j = 0
	h = 1
	p = 1
	q = 3
	while p < n:
		p *= q
		h += p
	c = n
	cp = c
	j = q - 1
	while h > 0 and risultato <= 0 and j < q:
		c = cp - (q - 1 - j) * h - 1
		while c <= 0:
			j = 0
			c = cp - (q - 1 - j) * h - 1
			while j < q and c <= 0:
			  j = j + 1
			  c = cp - (q - 1 - j) * h - 1
		if dato == x[c]: risultato = c
		else:
			if dato > x[c]:  j = j + 1 
			else:
				j = 0
				cp = c
				h = int(h / q)
	return risultato
	
lista = [-1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
dato = int(input('Introduci un numero '))
risultato = opzione_laterale(dato, lista)
if risultato < 0: print('Non trovato')
else: print('Trovato in posizione ', risultato)