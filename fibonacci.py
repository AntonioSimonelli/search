#!/usr/bin/python3
#
# File:     fibonacci.py
# Created:  17.06.2020
#

def ricerca_fibonacci(key, keys):
	k = 0
	if key > keys[len(keys) - 1]: return -1
	while fibo(k + 2) < len(keys): k = k + 1
	i = fibo(k)
	p = fibo(k - 1)
	q = fibo(k - 2)
	found = False
	k = 0
	while found == False and p > 1 and q > 0 and k < len(keys):
		if i < 0: return -1
		if key == keys[i]: found = True
		else:
			if key < keys[i]: i = i - q
			else: i = i + q
			tmp = p
			q = p - q
			p = tmp
			k = k + 1
	if found: return i
	else: return -1
	
def fibo(n):
    if n < 3: return 1
    else: return fibo(n - 1) + fibo(n- 2)
	
lista = [10, 20, 30, 40, 50, 60, 70]
dato = int(input('Introduci un numero '))
risultato = ricerca_fibonacci(dato, lista)
if risultato < 0: print('Non trovato')
else: print('Trovato in posizione ', risultato)