
#creando una lista ( se puede modificar)
lista = ["lucas dlato", "Soy Dalto",True,1.85,"Soy Dalto"]

#creando una tupla (no se puede modificar)
tupla = ("lucas dlato", "Soy Dalto",True,1.85,"Soy Dalto")

#esto es valido
#lista[3] = "maquinola"

#esto no es valido
#lista[3] = "maquinola"

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)

conjunto = {"lucas dlato", "Soy Dalto",True,1.85,"Soy Dalto"}

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict) ( la estrutura es key : value y separamos con comas)
diccionario = {
    "nombre":"lucas dlato",
    "alias":"Soy Dalto",
    "activo":True,
    "altura":1.85,
    "descripcion":"Soy Dalto"
}

print(diccionario["alias"])
print(lista[3])

