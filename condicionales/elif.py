ingreso_mensual = 81000
gasto_mensual = 80000

#if anidados y else is (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en dificit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien pa, estas bien")
    else:
        print("y pa, estas gastando una banda")

elif ingreso_mensual > 5000:
    print("estas bien economicamente en latinoamerica")

elif ingreso_mensual > 1000:
    print("estas bien economicamente en colombia")

elif ingreso_mensual > 200:
    print("estas bien economicamente en venezuela")

else: print("sos pobre")