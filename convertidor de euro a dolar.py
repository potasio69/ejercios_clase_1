

EURO_A_DOLAR = 0.90 
dolares = raw_input("Cuantos dolares deseas convertir a euros? :")
try:
    dolares = float(dolares)
except ValueError:
    print dolares, "Eso no es un numero campeon maquina figura crack mastodonte champion!"
else:
    print dolares, "dolares =", dolares * EURO_A_DOLAR
    print "euros"
print "Gracias!"
