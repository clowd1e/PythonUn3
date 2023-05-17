# list = [1, 2, 3, 4, 5]
# del list[4]
# print(list)

# def function(k):
#     if (k > 0):
#         result = k + function(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# function(6)

# def Fibonacci(n):
#     if n < 0:
#         print('Incorrect input')
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)

# print(Fibonacci(30))

# def myfunc(n):
#     return lambda a : a * n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(11))



# a = float(input('start: '))
# b = float(input('end: '))

# def average_value(x, y):
#     result = (x+y)/2
#     return result

# print(average_value(a, b))

# def choInke(par):
#     for i in range(0, par):
#         print(' ' * (par - i) + (' *' * i) + ' ')
# choInke(8)

# import random

# def prOg(par):
#     x = []
#     s = ''
#     for i in range(par):
#         x.append(random.randint(1,50))
#     for i in x:
#             s = s + ' ' + str(i)
#     return s
# a = prOg(10)
# print(a)
import random
names = ["Jan", "Magda", "Karolinka"]
surnames = ["Kowalski", "Pych", "Kowal"]


def zapelniacz(n):
    lista = []
    for i in range(n):
        wiek = random.randint(18, 70)
        tel = random.randint(5000000, 8000000)
        lista.append(
            {"name": names[random.randint(0, len(names)-1)], "surname": surnames[random.randint(0, len(surnames)-1)],
             "age": wiek, "phone": tel})
    return lista

def wypisywacz(tablica):
    for i in tablica:
        print(i)

def szukaj(s,tablica):

    for i in tablica:
        for j in i.keys():
            if s.lower() == str(i[j]):
                print(i, i.keys())



tab = zapelniacz(10)
wypisywacz(tab)
szukaj(input("wprowadz imie"),tab)