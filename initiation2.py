mon_nombre = 42
mon_autre_nombre = 1.414
un_mot = "bonjour"
un_autre_mot = "toto"

print(un_autre_mot)

une_liste = [10, 20, 30, 'a', 'b', "bonjour", [1, 5, 25]]

print(une_liste)

somme = mon_nombre + mon_autre_nombre
print(somme)

somme = un_mot + un_autre_mot
print(somme)

somme = str(mon_nombre) + un_mot
print(somme)

une_chaine = "57"

somme = mon_nombre + int(une_chaine)
print(somme)

somme = une_liste + [45]
print(somme)