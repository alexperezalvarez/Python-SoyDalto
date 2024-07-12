diccionario = {
    "nombre":"breynner",
    "apellido" :"perez",
    "pais"     : "colombia"
}

#nos devuelve un objeto dict_items 
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_ddffgfg = diccionario.get("ddffgfg")
print("el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemnto del diccionario 
diccionario.pop("pais")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)