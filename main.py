print("Hello")

a = int(input("Podaj ilość:"))

for x in range(a):
    print(x)

print("Zmienna licznik po zakończeniu = ", x)


# tu będzie funkcja
def doKwadratru(x):
    return x ** 2


print(x, "do kwadratu = ", doKwadratru(x))
