print("Bienvenue dans la troisième.")

entree = input("Quel est votre nom: ")
print("Bonjour, vous vous appelez",entree + ".")

age = int(input("Quel est votre age: "))
print("Vous avez", age, "an(s).")

# Instruction conditinnelle
if age >= 18:
    print("Vous êtes majeur.") # indentation
    print("A bientôt.")
else:
    print("Vous n'êtes pas majeur.")