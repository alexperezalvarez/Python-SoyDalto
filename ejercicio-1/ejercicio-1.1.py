#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos

crudo_promedio = 5 
crudo_dalto = 3.5 

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 -  otros_cursos_promedio *1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 -  dalto_curso *1000 // crudo_dalto / 10

#Diferencias de duracion

diferencias_con_min = 100 - dalto_curso / otros_cursos_min *100
diferencias_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencias_con_promedio = 100 - dalto_curso / otros_cursos_promedio *100

#Mostrando las diferencias de durancion (Ejecicio A )
print('--------------')
print('el curso de dalto dura: ')
print(f' - un {diferencias_con_min}% menos que el mas rapido')
print(f' - un {diferencias_con_max}% menos que el mas lento')
print(f' - un {diferencias_con_promedio}% menos que el promedio')
print('-------------')

#Mostrando la cantidad de espacios vacios que se remueven (ejecicio B)
print(f'El curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio ')
print(f'Este curso elimino el  {tiempo_vacio_dalto}% de tiempo vacio ')
print('----------------')

#Mostrando la diferencia si los cursos duran 10 hora
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio *1000// dalto_curso / 100} horas de otros cursos')
print('-----------------')