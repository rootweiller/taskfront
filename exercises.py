#!/usr/bin/python3

#Ejercicios de la 2da fase 



def duplicate_list():

	strings = raw_input("Insert caracters: ")


	strings = list(set(strings))

	print strings


foo = duplicate_list()




def integer_number():


	A = []


	# Limit of for

	C = input("Insert Limit for: ")

	for i in range(0,C):

		A.append(input("Insert Integer: "))

	m = filter(lambda elem: elem[1] % 10 == 0, enumerate(A))

	if m:

		print ("2", m)

	else:

		print("-1", m)

foo = integer_number()



