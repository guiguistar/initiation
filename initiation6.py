print("Débuter en programmation")

print("Boucle while")

debut = 2
fin = 20
pas = 1

n = debut #compteur
while n < fin:
    print("n =", n)
    n += pas
    
print("Boucle for")
for n in range(debut, fin, pas):
    if n == 9:
        continue
    if n == 13:
        break
    print("n =", n)
else:
    print("Sortie de boucle naturelle.")
    
for compteur in range(100,0,-5):
    print("compteur :", compteur)