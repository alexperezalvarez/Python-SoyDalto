cadena1 = "Hola,Soy,Dalto"
cadena2 = "Bienvenido maquinalo"

#convertir a mayusculas
mayusc = cadena1.upper()

#convertir a mayusculas
minusc = cadena1.lower()

#primera letra en mayuscula
primera_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busquedad_find = cadena1.find("r")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("a")

#si es numerico devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos  las coincidencias de una cadena dentro de otra cadena devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("d")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("Hola")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("o")

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace(",", "")
cadena_nueva_2 = cadena_nueva.capitalize()

#separa cadenas con la cadena que le pasemos
separar_cadenas = cadena1.split(",")

print(separar_cadenas[0])
