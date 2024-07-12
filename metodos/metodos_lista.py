
#Creando una lista con list()
lista = list([200,20, True, False])

#devuelve la cantidad  de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista 
lista.append(89)

#agrando un elemento a la lista en un indice especifico
lista.insert(2, "TOMA MAMA")

#agregando varias elemtos a la lista
lista.extend([False, 2030])

#elimiando un elemnto de la lista (por su indice)
lista.pop(-2) #-1 para eliminar el ultimo, -2 para eliminaer anteultimo y asi sucesivamente

#removiendo un elemento de la lista (por su valor)
lista.remove("TOMA MAMA")

#eliminado todos los elementos de la lista
#lista.clear()

#Ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(200)

print(elemento_encontrado)