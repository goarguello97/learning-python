### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


fizz_buzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (string) y retorne
verdadero o falso (bool) según sean o no anagramas.
- Un anagrama consiste en formas una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamentes iguales no son anagrama.
"""


def is_anagram(word_a, word_b):
    if word_a.lower() == word_b.lower():
        return False
    return sorted(word_a.lower()) == sorted(word_b.lower())


result = is_anagram("coca", "caco")
print(result)

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que impa los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""


def fib():
    a = 0
    b = 1
    aux = 0
    for i in range(0, 50):
        print(a)
        aux = a+b
        a = b
        b = aux


fib()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho eso, imprime los números primos entre 1 y 100.
"""


def is_prime():
    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for i in range(2, number):
                if number % i == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)


is_prime()

"""
Crea un programa que inviarta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def reverse_string(string):
    aux = ""
    for caracter in range(len(string)-1, -1, -1):
        aux += string[caracter]

    return aux


print(reverse_string("Hola mundo"))
