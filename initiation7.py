
pi = 3.14159265359

rayon = 3.54
aire = pi * rayon * rayon

def aireDisque(r):
    return pi * r * r

aire2 = aireDisque(3.54)
aire3 = aireDisque(4)

"""
Fonction qui compre le nombre de voyelles dans
une chaine de caracteres.
"""
def voyelles(chaine):
    compteur = 0
    for caractere in chaine:
        if caractere in "aeiouy":
            compteur += 1
    return compteur

print(voyelles("bonjour"))
print(voyelles("tototututiti"))
print(voyelles("aeiou"))


"""
0 1 1 2 3 5 8 13 ...

"""
def fibo(n):
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(n-1):
        a, b = b, a + b
    return b

for i in range(8):
    print(fibo(i))
        
    