while True:
    try:
        entier = int(input("Nombre entier:"))
        if entier == 0:
            break
    except ValueError:
        print("Nombre entier...")
    except KeyboardInterrupt:
        print("Sortie demande au clavier: Ctrl + C")
        print("Ciao")
        break
    else:
        print("Ni erreur de valeur, ni erreur clavier.")
    finally:
        print("Fin d'iteration.")
