def Factorielle(nombre):
	if nombre <= 1:
		return 1
	else:
		return nombre * Factorielle(nombre-1)



print(Factorielle(5))