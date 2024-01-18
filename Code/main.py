#import doc + fichier fonctions
from functions import*







#------debut -->




#ajouter le num de sortie .............................................

print("Bienvenue dans notre bibliothèque")
menu=1
while menu!=0:
    menu = choix_menu()
    #------saisie sécurisé et action a faire pour le menu 1

    if menu ==1 :
        action=action_M1()


    #------choix des fonctions pour l action a réalisé
        if action ==1:
            #fonction pour ajouter un lecteur
            ajouter_lecteur()
        elif action ==2 :
            #fonction pour afficher un lecteur
            afficher_lecteur()
        elif action==3:
            #fonction pour modifier un lecteur
            modifier_lecteur()
        elif action ==4 :
            #fonction pour supprimer un lecteur
            supprimer_lecteur()






    #------saisie sécurisé et action a faire pour le menu 2
    elif menu ==2 :
        action=action_M2()

        # ------choix des fonctions pour l action a réalisé
        if action==1:
            #fonction pour afficher un livre
            afficher_livre()
        elif action == 2 :
            #fonction pour ajouter un livre
            ajouter_livre()
        elif action == 3:
            #fonction pour modifier un livre
            modifier_livre()
        elif action ==4:
            #fonction pour supprimer un livre
            supprimer_livre()




    #------saisie sécurisé et action a faire pour le menu 3
    elif menu == 3 :
        action=action_M3()

        # ------choix des fonctions pour l action a réalisé
        if action==1:
            #fonction pour noter un livre
            noter_livre()
        if action==2:
             #fonction pour suggerer un livre
            similarité()
            suggérer_livre()