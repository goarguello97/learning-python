### Functions ###


def my_function():
    print("Esto es una función")


my_function()
my_function()
my_function()


def sum_two_values(a, b):
    print(a + b)


sum_two_values(2, 10)
sum_two_values("2", "10")
sum_two_values(5.2, 6.8)


def sum_two_values_with_return(a, b):
    return a + b


my_result = sum_two_values_with_return(4, 5)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")


print_name("Gonzalo", "Argüello")
print_name(surname="Argüello", name="Gonzalo")


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Gonzalo", "Argüello")
print_name_with_default("Gonzalo", "Argüello", "GONZAARGUELLO")


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "Test")
print_upper_texts("Hola")
