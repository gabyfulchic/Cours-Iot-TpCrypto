#!/usr/bin/python3.5
#-*- coding: utf-8 -*-

import cryptocompare as crypt

#pip3 install -U lazyme
from lazyme.string import color_print

#On affiche toutes les cryptomonnaies sous forme d'une liste
monnaies = crypt.get_coin_list()

for key in monnaies:

	color_print(key, color='green') #on peut aussi faire print(key, end=', ') pour éviter le saut de ligne

print('######################################################')
print(' ------------------------------------------------------')
color_print('|Saisie le nom de la cryptomonnaie que tu veux ou alors|', color='red')
color_print('|        saisie list pour les afficher toutes !        |', color='red')
print(' ------------------------------------------------------')
print('######################################################')


#boucle permettant la demande de crypto à afficher, qui se break si l'on écrit quit
while 1 :

	entree = input('Saisie un des noms de la liste ou quit pour arréter ! ')

	if entree!='quit':

		price = crypt.get_price(entree)
		color_print('Prix de {} : {}€ '.format(entree, price), color='green')

	else:

		break
