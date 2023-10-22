# 1. Ejercicio: Dado un número, imprime si es positivo o negativo. 
# 2. Ejercicio: Dado un número, imprime si es par o impar.
# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
numero = 24
if numero > 0:
  print ("positivo")
else:
  print ("negativo")
numero = 12
if numero % 2 == 0:
    print ("par")
else:
    print ("Impar")
a, b, c = 4, 6 ,1
mayor = max(a,b,c)
print (mayor)
