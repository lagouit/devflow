def menu():
    print("1. Ajouter client")
    print("2. Ajouter produit")
    print("3. Créer facture")
    print("4. Quitter")

while True:
    menu()
    choix = input("Choix : ")
    if choix == "4":
        break

clients = {}

def supprimer_clienr():
    code = input("Code client : ")
    nom = input("Nom : ")
    clients[code] = {"nom": nom}
    print("Client supprimer")
