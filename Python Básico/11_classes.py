### Clases ###

class MyEmptyPerson:
    pass


print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada
        self.__surname = surname  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name}, está caminando.")


my_person = Person("Gonzalo", "Argüello")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Gonzalo", "Argüello", "GONZA")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Homero Simpsons (Padre de Bart)"
print(my_other_person.full_name)
my_other_person.walk()
