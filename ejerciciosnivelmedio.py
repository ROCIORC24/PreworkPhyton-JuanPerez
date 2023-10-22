"""1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
11. Ejercicio: Define una función que tome una cadena y determine si es un 1. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
"""
def fibonacci (n):
  a,b = 0,1
  for i in range(n):
    print(a, end=" ")
    a,b = b, a+ b
fibonacci (10)

def divisores (n):
  return [i for i in range(1, n+1) if n % i==0]
print (divisores(12))

def unicos (lista):
  return list (set(lista))
print (unicos([1,2,3,3,2,4,4]))

def suma_digitos(n):
  return sum(int(digito) for digito in str(n))
print (suma_digitos(123))

def contar_vocales(cadena):
  return sum(1 for letra in cadena if letra. lower () in  "aeiou")
print(contar_vocales("Hola Mundo"))

def primeros_n_elementos (lista, n):
  return lista[:n]
print (primeros_n_elementos([1,2,3,4,5], 3))

def contar_mayusculas_minusculas (cadena):
  mayusculas = sum(1 for letra in cadena if letra.isupper())
  minusculas = sum(1 for letra in cadena if letra.islower())
print (contar_mayusculas_minusculas("HgUGDGgfhvbslhJGh"))

def es_perfecto(num):
  return num == sum(divisor for divisor in range(1, num) if num % divisor == 0)
print (es_perfecto(6))

def a_binario(n):
  return bin(n).replace("0b", "")
print (a_binario(5))

def interseccion(list1, list2):
  return list (set(list1)& set(list2))
print (interseccion([1,2,3,4], [2,7,4,8]))

def es_palindromo(cadena):
  return cadena == cadena [::-1]
print(es_palindromo("ordenador"))

for i in range (1, 51):
  if i%3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i%5 == 0:
    print("Buzz")
  else:
    print(i)
    
def ordenar_lista(lista):
  return sorted (lista)
print (ordenar_lista([4,7,6,8,9,2,4,6,7,2,1]))

def filtrar_palabras(lista_de_palabras, n):
  return[palabra for palabra in lista_de_palabras if len(palabra)>n]
print(filtrar_palabras(["casa","colegio", "ordenador", "clase"], 6))

def serie_fibonacci(n):
  if n<=0:
    return[]
  elif n== 1:
    return[0]
  fib = [0,1]
  while len(fib) < n:
    fib.append(fib[-1]+ fib[-2])
  return fib
print (serie_fibonacci(10))

def maximo(lista):
  return max (lista)
print (maximo([2,6,3,9]))

def suma_cubos_digitos(n):
  return sum(int(digit)**3 for digit in str(n))
print(suma_cubos_digitos(123))

def segundo_maximo (lista):
  return sorted (set(lista), reverse=True)[1]
print (segundo_maximo([2,5,7,8,4,4,9]))

def tienen_comun (lista1, lista2):
  return bool (set (lista1) & set(lista2))
print(tienen_comun ([4,5,6],[6,7,8]))

def invertir_lista (lista):
  return lista[::-1]
print(invertir_lista([1,2,3,4,5]))

def contar_digitos_letras (cadena):
  digitos =sum(c.isdigit() for c in cadena)
  letras =sum (c.isalpha() for c in cadena)
  return digitos, letras
print(contar_digitos_letras("Programación"))

def suma_acumulada(lista):
  total = 0
  suma_acumulada = []
  for numero in lista:
    total += numero
    suma_acumulada.append(total)
  return suma_acumulada
print (suma_acumulada([1, 2, 3, 4, 5]))

from collections import Counter
def elemento_mas_comun(lista):
  return Counter(lista). most_common (1)[0][0]
print (elemento_mas_comun([4,5,7,1,2,4,1,9,8]))

def tabla_de_multiplicar (numero):
  return{i:numero * i for i in range (1,11)}
print(tabla_de_multiplicar(8))

def contar_caracteres(cadena):
  return {caracter: cadena.count(caracter) for caracter in cadena}
print(contar_caracteres("Buenas tardes profesores"))

def elementos_no_comunes(lista1, lista2):
  return list(set(lista1)^set(lista2))
print(elementos_no_comunes([1,2,3,4,5],[4,5,6,7,8]))

def eliminar_duplicados (lista):
  return list (set(lista))
print (eliminar_duplicados([5,6,5,6,4,3,7,8]))

def suma_cuadrados_pares(n):
  return sum(i**2 for i in range(2, n+1, 2))
print(suma_cuadrados_pares(6))

def promedio(lista):
  return sum(lista)/ len(lista)
print (promedio([1,2,3,4,5]))

def cadena_mas_larga(lista):
  return max(lista, key=len)
print(cadena_mas_larga (["ordenador","programacion","phyton"]))  

def es_primo(num):
  if num < 2:
   return False
  for i in range (2, int (num ** 0.5) +1):
   if num % i == 0:
     return False
     return True
   
def primeros_n_primos(n):
  primos = []
  numero = 2
  while len(primos) < n:
    if es_primo(numero):
      primos.append (numero)
    numero += 1
  return primos
print (primeros_n_primos(5))

def invertir_palabras(cadena):
  return " ". join(cadena.split ()[::-1])
print (invertir_palabras ("Buenas tardes"))

def ordenar_por_ultimo_elementos(tuplas):
  return sorted (tuplas, key=lambda x: x[-1])
print (ordenar_por_ultimo_elementos ([(1,2), (5,7),(7,8)]))
    
def contar_vocales (cadena):
  return sum (1 for c in cadena. lower () if c in "aeiou")
print (contar_vocales ("Buenas tardes, hace un tiempo muy bueno"))

def es_primo(num):
  if num <2:
    return False
    for i in range(2, int(num ** 0.5)+1):
       if num % i == 0:
          return False
          return True
print (es_primo(17))

    
  
  
  



  
  




  