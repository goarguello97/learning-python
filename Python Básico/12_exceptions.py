### Exception Handling ###

a = 5
b = 1
b = "1"

# try except

try:
    print(a + b)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción.
    print("Se ha producido un error")

# try except else finally

try:
    print(a + b)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción.
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(a + b)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(a + b)
    print("No se ha producido un error")
except ValueError as error:  # Capturamos un error en específico
    print(error)
except Exception as exception:  # Capturamos un error en general
    print(exception)
