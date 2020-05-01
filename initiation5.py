reponse = 'hibou'
vies = 10

while vies > 0:
    proposition = input("Votre proposition: ")
    if proposition == 'stop':
        print("A bientot.")
        break
    if proposition == 'pass':
        continue
    if proposition > reponse:
        print("La reponse se situe avant.")
    if proposition < reponse:
        print("La reponse se situe apres.")
    if proposition == reponse:
        print("Vous avez gagne!")
        break # sort de la boucle
    vies -= 1 #vies = vies - 1
    print("Nombre de vies restante(s):", vies)
else: # ne s'execute qu'en cas de sortie naturelle de la boucle
    print("Vous avez perdu.")