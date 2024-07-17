frase = input(" decime una frase: ")
palabras_seperadas = frase.split(" ")
cantidad_de_palabras = len(palabras_seperadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en dicirlo')
print(f'Dalto lo diria en {cantidad_de_palabras *100 // 2 *1.3 / 100} segundos')
if cantidad_de_palabras > 120:
    print("para flaco tampoco de pedi un testamento")