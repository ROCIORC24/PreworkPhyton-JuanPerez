#1. Ejercicio: Define una función que tome dos números y retorne su suma.
# 2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
# 3. Ejercicio: Define una función que tome un número y determine si es primo.
#4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
#5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
def suma (a, b):
  return a + b
print (suma (4, 2))

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial (n - 1)
print(factorial(5))

def es_primo (num):
  if num < 3:
    return False
  for i in range (3, num):
    if num % 1 == 0:
     return False
  return True
print (es_primo(7))

def sumar_lista (lista):
  return sum (lista)
print (sumar_lista([1,2,3,4,5,6]))

def reversa(cadena):
  return cadena [:: -1]
print(reversa ("HOLA"))
