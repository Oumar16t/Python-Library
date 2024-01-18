# fonction choix du menu --> retourne le numero du menu correspondant
from math import *
import time
#block 0 --> Les fonctions permettent a l'utilisateur de choisir l'action qu'il veut effectuer ----------------------------------------------------
'''La fonction choix_menu nous permet d'orienter l'utilisateur vers une des parties du sujet --> les lecteurs, les livres et la suggéstion '''
def choix_menu():
    print("----------          ----------")
    print("que voulez-vous faire ?")
    print("dans quel menu voulez vous aller ?")
    print("0.sortir    1.Profils des lecteurs    2.Visiter le dépôt des livres    3.Recommandation")
    # ------choix menu, saisie sécurisé------
    menu = int(input(" saisissez le chiffre correspondant au menu choisit : "))
    while menu < 0 or menu > 3:
        print("les saisies possible sont de 0 à 3")
        menu = int(input(" saisissez le chiffre correspondant au menu choisit : "))
    return menu
'''Les 3 fonctions actions permettent d'orienter l'utilisateur vers l'action (justement) qu'il veut effectuer-------------'''
'''La fonction M1 est associé au profils des lecteurs. Elle permet de rediriger les utilisateur vers les fonctions ajouter_lecteur,
afficher_lecteur,modifier_lecteur et supprimer_lecteur'''
def action_M1():
    print("----------          ----------")
    print("vous êtes dans le profils des lecteurs")
    print("quelle action voulez vous effectuer ?")
    print("0.retour    1.ajouter un lecteur    2.afficher un lecteur    3.modifier un lecteur    4.supprimer un lecteur")
    action = int(input(" saisissez le chiffre correspondant à l'action choisit : "))
    while action < 0 or action > 4:
        print("les saisies possible sont de 0 à 4")
        action  = int(input(" saisissez le chiffre correspondant à l'action choisit : "))
    return action

'''La fonction M2 est associé au livres. Elle permet de rediriger l'utilisateur vers les fonctions afficher_livre,
ajouter_livre, modifier_livre et supprimer_livre'''
def action_M2():
    print("----------          ----------")
    print("vous êtes dans le dépôt des livres")
    print("quelle action voulez vous effectuer ?")
    print("0.retour    1.afficher les livres    2.ajouter un livre    3.modifier un livre   4.supprimmer un livre   ")
    action = int(input(" saisissez le chiffre correspondant à l'action choisit : "))
    while action < 0 or action > 4:
        print("les saisies possible sont de 0 à 4")
        action = int(input(" saisissez le chiffre correspondant à l'action choisit : "))
    return action

''' La fonction M3 est associé à la recommandation. Elle permet de rediriger l'utilisateur vers les fonctions noter_livre et
 suggérer livre'''
def action_M3():
    print("----------          ----------")
    print("vous êtes dans les Recommandations")
    print("quelle action voulez vous effectuer ?")
    print("0.retour    1.noter un livre    2.suggérer un livre  ")
    action = int(input(" saisissez le chiffre correspondant à l'action choisit : "))
    while action < 0 or action > 2:
        print("les saisies possible sont de 0 à 2 ")
        action = int(input(" saisissez le chiffre correspondant à l'action choisit : "))
    return action

#-------------------------------------------------------------------------------------------------------------
#Partie 1 --> Profils des lecteurs
#La fonctions action_M2 donne l'accées au fonctionbs de cette partie. La partie profils lecteurs
'''La première fonctions, ajouter_lecteur permet comme son nom l'indique d'ajouter un nouveau lecteur.
Les fichiers modifiés sont --> readers.txt, booksread.txt et matrice_note.'''
def ajouter_lecteur():
    print("----------          ----------")
#ouverture de readers.txt de façon à se qu'il puisse être lu et modifier.
    with open("readers.txt", "a") as f,open ("readers.txt","r") as f1:
        book = open("books.txt", "r")
#cette partie permet de verifié si le pseudo du nouveau profil n'existe pas deja.
        l=[]
        ligne=f1.readline()
        while ligne!="":
            ligne=ligne.split(",")
            l.append(ligne)
            ligne=f1.readline()
        if len(l)>0:

            if "\n" not in l[len(l)-1][3]:
                f.write('\n')
            pseudo = str(input("Saisir votre pseudo : "))
            for i in range (len(l)):
                if l[i][0]==pseudo:
                    print("Le pseudo existe deja ")
                    print("Vous allez être redirigé vers le menu ")
                    time.sleep(5)
                    return
        else:
            pseudo = str(input("Saisir votre pseudo : "))
#Si le pseudo est bien nouveau alors cette partie demande les caracteristique du nouveau profil à l'utilisateur
        f.write(pseudo)
        f.write(",")
        print('\n')
        print("quel est votre genre")
        print("1.homme    2.femme")
        n = int(input("saisissez le nombre correspondant au genre choisis : "))
        while n < 1 or n > 2:
            print("les saisies possible sont de 1 à 2")
            n = int(input("saisissez le nombre correspondant au genre choisis : "))
        # La variable y permet de changer le type de n ainsi nous pouvons faire la saisie sécurisé grace a n et ecrire le résultat grace a y
        y = str(n)
        f.write(y)
        f.write(",")
        print('\n')
        print("quel age avez-vous ?")
        print("1.<=18 ans    2.>18 et <25 ans    3.>25 ans")
        n = int(input("saisissez le nombre correspondant à l'âge choisis : "))
        while n < 1 or n > 3:
            print("les saisie possible sont de 1 à 3 : ")
            n = int(input("saisissez le nombre correspondant à l'âge choisis : "))
        y = str(n)
        f.write(y)
        f.write(",")
        print('\n')
        print("quel est votre style de lecture ? ")
        print("1.Science-fiction    2.Biographie    3.Horreur    4.Romance")
        print("5.Fable    6.Histoire    7.Comedie")
        n = int(input("saisissez le nombre correspondant au style de lecture : "))
        while n < 1 or n > 7:
            print("Les saisie possible sont de 1 à 7 : ")
            n = int(input("saisissez le nombre correspondant au style de lecture : "))
        y = str(n)
        f.write(y)
        f.write("\n")
#ouverture du fichier booksread.txt afin qu'il puisse être lu et modifié
    with open("booksread.txt", "a") as f,open ("booksread.txt","r") as f1:
#cette partie verifie si un saut de ligne est a effectué dans le fichier avant d'écrire le nouveau pseudo dans celui-ci
        l = []
        ligne = f1.readline()
        while ligne != "":
            l.append(ligne)
            ligne = f1.readline()
        if len(l) > 0:
            if "\n" not in l[len(l) - 1]:
                f.write('\n')
        f.write(pseudo)
#Cette partie permet d'afficher les livres avec un indice afin de facilité leurs utilisation.
        print("Quel livre avez-vous lu ?")
        l = []
        ligne = book.readline()
        while ligne != "":
            l.append(ligne)
            ligne = book.readline()
        for i in range(1,len(l)+1):
            print(i, ".", l[i-1])
#cette partie ajoute les livres lu par l'utilisateur au fichier booksread.txt
        print("combien de livre avez-vous lu ?")
        n = int(input("saisissez le nombre de livre : "))
        while n < 0 or n > len(l):
            print("les saisies possible sont entre 0 et ",len(l))
            n = int(input("saisissez le nombre de livre : "))
        if n != 0:
            for i in range(n):
                nl = int(input("saisir l'indice du livre lu : "))
                while nl < 1 or nl > len(l):
                    print("les saisies possible sont entre 0 et ",len(l))
                    nl = int(input("saisir l'indice du livre lu : "))
                y = str(nl)
                f.write(",")
                f.write(y)

#cette partie permet de mettre les livre contenu dans le fichier books.txt sous forme de liste
        l=[]
        m=[]
        ligne=book.readline()
        while ligne!="":
            l.append(ligne)
            ligne=book.readline()
    book.close()
#ouverture des fichiers permettant la lecture et la modification du fichier matrice_note
    book = open("books.txt", "r")
    with open ("matrice_note","a") as f, open ("matrice_note","r") as f1:

#cette partie vérifie si un saut de ligne est necessaire avant l'ajout de la nouvelle ligne correspondant au nouveau lecteur
        nl=[]
        b=[]
        ligne = f1.readline()
        while ligne != "":
            nl.append(ligne)
            ligne = f1.readline()
        if len(nl)>0:
            if "\n" not in nl[len(nl) - 1]:
                f.write('\n')
        ligne=book.readline()
        while ligne!="":

            b.append(ligne)
            ligne=book.readline()

        for i in range (len(b)):
            m.append(str(0))
        m=" ".join(m)
        f.write(m)
    print("Votre profil a bien été ajouter")
    book.close()




'''cette fonction est en une seule partie. Le while fait defilé les lignes. Les ifs testent si la ligne et celle choisis
par l'utilisateur. Si la ligne est bonne alors son profil est afficher sinon la boucle est casser une fois que le fichier
est parcouru en entier'''
def afficher_lecteur():
    print("----------          ----------")
    with open("readers.txt", "r") as f:
        choix = 0
        pseudo = str(input("saisissez le pseudo du profil a afficher : "))
        while choix == 0:
            ligne = f.readline()
            ligne = ligne.split(",")
            if pseudo == ligne[0]:

                if "1" in ligne[1]:
                    print("le lecteur est un homme")
                else:
                    print("le lecteur est une femme")

                if "1" in ligne[2]:
                    print("le lecteur a 18 ans ou moins ")
                elif "2" in ligne[2]:
                    print("le lecteur a entre 19 et 25 ans ")
                else:
                    print("le lecteur a plus de 25 ans ")

                if "1" in ligne[3]:
                    print("le style de lecture est science-fiction ")
                elif "2" in ligne[3]:
                    print("le style de lecture est biographie ")
                elif "3" in ligne[3]:
                    print("le style de lecture est horreur")
                elif "4" in ligne[3]:
                    print("le style de lecture est romance")
                elif "5" in ligne[3]:
                    print("le style de lecture est fable")
                elif "6" in ligne[3]:
                    print("le style de lecture est histoire")
                else:
                    print("le style de lecture est comedie")

                choix = 1
            ligne="".join(ligne)
            if ligne == "":
                choix = 1
                print("le profil n'existe pas")
                print("Vous aller être rediriger vers le menu")
                time.sleep(5)






'''Cette fonction est en trois partie. tout d'abord une première fonction qui va vérifié si un profil contenant le pseudo
fournit par l'utilisateur existe ensuite une fonction modifiant le fichier readers.txt pour finir par une fonction modifiant
le fichier booksread.txt'''

def modifier_lecteur():
    print("----------          ----------")
    with open("readers.txt", "r") as f:
#Cette partie vérifie l'existance d'un profil contenant le pseudo fournit par l'utilisateur
        print("Quel est le pseudo du profil que vous voulez modifier ?")
        pseudo = input("Saisir le pseudo : ")
        ligne = f.readline()
        choix = 0
        while choix == 0 and ligne != "":

            ligne=ligne.split(",")
            if pseudo ==ligne[0]:
                choix = 1
            ligne = f.readline()
        if choix ==0:
            print("le profil n'éxiste pas")
            print("Vous allez être redirigé vers le menu")
            time.sleep(5)
            return
#cette partie deamnde le nouveau pseudo du profil
        print("voulez vous changer le pseudo de l'utilisateur ?")
        choix = " "
        while choix != "oui" and choix != "non":
            choix = input("saisir oui ou non : ")
        if choix == "oui":
            pseudo_2 = input("saisir le nouveau pseudo: ")
        else:
            pseudo_2=pseudo

#appel des deux sous fonctions
        change_readers(pseudo,pseudo_2)
        change_booksread(pseudo,pseudo_2)




#Cette sous fonction permet de modifier les informations du ficchiers readers.txt
def change_readers(pseudo,pseudo_2):
    '''Cette partie crée une liste qui contiendra les nouvelles informations du profil et crée une autre list contenant les
    informations du fichiers.'''
    with open("readers.txt","r") as f :
        profil=""
        l=[]
        ligne=f.readline()
        j=0
        while ligne!="":
            l.append(ligne)
            if pseudo in ligne :
                profil=ligne
                profil = profil.split(",")
                profil[0]=pseudo_2
                n=j
            ligne=f.readline()
            j=j+1
    if profil=="":
        return
#Cette partie modifie les information du profil et les stock dans la liste profil.
#La variable y permet d'effectiuer des saisies sécuriser tout en complétant la loiste avec des str

    print("voulez vous changer le genre du profil ?")
    choix=" "
    while choix != "oui" and choix != "non" :
        choix=input("saisir oui ou non : " )
    if choix=="oui":
        print("quel est le genre du profil")
        print("1.homme    2.femme")
        y = int(input("saisissez le nombre correspondant au genre choisis : "))
        while y < 1 or y > 2:
            print("les saisies possibles sont de 1 à 2")
            y = int(input("saisissez le nombre correspondant au genre choisis : "))
        profil[1]=str(y)
    print("voulez vou changer l'age du profil ?")
    choix=" "
    while choix != "oui" and choix != "non" :
        choix=input("saisir oui ou non : " )
    if choix=="oui":
        print("quel est l'age du profil ?")
        print("1.<=18 ans    2.>18 et <25 ans    3.>25 ans")
        y = int(input("saisissez le nombre correspondant à l'âge choisis :"))
        while y < 1 or y > 3:
            print("les saisie possible sont de 1 à 3")
            y = int(input("saisissez le nombre correspondant à l'âge choisis :"))
        profil[2]=str(y)
    print("voulez vous changer le style de lecture du profil ? ")
    choix=" "
    while choix != "oui" and choix != "non" :
        choix=input("saisir oui ou non : " )
    if choix == "oui":
        print("quel est le style de lecture ? ")
        print("1.Science-fiction    2.Biographie    3.Horreur    4.Romance")
        print("5.Fable    6.Histoire    7.Comedie")
        y = int(input("saisir le nombre correspondant au style de lecture : "))
        while y < 1 or y > 7:
            print("Les saisie possible sont de 1 à 7")
            y = int(input("saisir le nombre correspondant au style de lecture : "))
        profil[3]=str(y)
    profil=",".join(profil)
    profil=profil.rstrip()
    l[n]=profil+'\n'
    #cette partie réécrie le dossier precedement stocker dans la liste l.
    with open ("readers.txt","w")as f :
        for i in range (len(l)):
            f.write(l[i])


#Cette sous fonctions permet de modifier le informations du fichier booksread.txt et matrice_note

def change_booksread(pseudo,pseudo_2):
    with open ("booksread.txt","r") as f :
#Cette partie stock le fichier dans une liste en changeant le pseudo du profil si il y a eu changement.
        ligne = f.readline()
        l=[]
        j=0
        while ligne!= "":
            ligne=ligne.rstrip()
            ligne=ligne.split(",")
            if pseudo in ligne[0]:
                p=j
                ligne[0]=pseudo_2
                l.append(ligne)
            else :
                l.append(ligne)
            j=j+1
            ligne=f.readline()
#Cette Partie demande a l'utilisateur si il veut changer ces livres lu et affiches les livres si la reponse est positive
    print("voulez-vous changer les livres que vous avez lu ? ")
    choix = " "
    while choix != "oui" and choix != "non":
        choix = input("saisir oui ou non : ")
    if choix == "non":
        with open("booksread.txt", "w") as f:

            for i in range(len(l)):
                l[i] = ",".join(l[i])
                f.write(l[i] + '\n')
        print("Les modifications ont bien été apportées")
        print("Vous aller être rediriger vers le menu")
        time.sleep(5)
        return
    z = [pseudo_2]
    l[p] = z
    with open ("books.txt","r") as f :
        lbooks=[]
        ligne=f.readline()
        while ligne!="":
            lbooks.append(ligne)
            ligne=f.readline()
        for i in range (len(lbooks)):
            print(i+1,". ",lbooks[i])
#Cette partie stock les nouveaux livres lu par le profil dans la liste avant de réécrire le fichier booksread.txt
    print("combien de livre avez-vous lu ?")
    n=int(input("saisir le nombre de livre : "))
    while n<1 or n>len(lbooks) :
        n=int(input("saisir le nombre de livre : "))
    for i in range(n):
        print("saisissez le numero du livre que vous avez lu")
        y = int(input())
        while y < 0 or y > len(lbooks) :
            y = int(input("saisir un numero de livre"))
        l[p].append(str(y))
    with open ("booksread.txt","w") as f :

        for i in range (len(l)):
            l[i]=",".join(l[i])
            f.write(l[i]+'\n')
#CEtte partie met la ligne du nouveau profil a 0
    with open ("matrice_note","r") as f :
        print("Les modifications ont bien été apportées")
        print("Les notes des livres vont etre remises a 0")
        print("Vous aller être rediriger vers le menu")
        time.sleep(5)
        M=[]
        ligne=f.readline()
        cpt=0
        while ligne!="":
            ligne=ligne.rstrip()
            ligne=ligne.split(" ")
            if cpt==p:

                for i in range (len(ligne)):
                    ligne[i]="0"
            ligne=" ".join(ligne)
            M.append(ligne)
            ligne=f.readline()
            cpt=cpt+1
    with open ("matrice_note","w") as f :
        for i in range (len(M)):
            f.write(M[i]+'\n')


#Cette fonction permet de supprimer un lecteur en le suprimant de 3 dossiers, booksread.txt, readrs.txt et matrice_note
#La méthode est la même pour les deux premier fichier. on ecrit le fichier dans une liste ou l on ne mets pas
#Le profil voulant etre enlevé avant de réecrire le fichier
def supprimer_lecteur():
    print("----------          ----------")
    print("Quel est le pseudo du lecteur ?")
    pseudo=input("Saisir pseudo : ")
#Cette partie modifie le fichie readers.
    with open ("readers.txt","r") as f :
        l=[]
        choix=0
        ligne=f.readline()
        k=0
        while ligne!="":
            ligne=ligne.rstrip()
            ligne=ligne.split(",")
            if pseudo == ligne[0]:
                n=k
                choix=1
            else :
                ligne=",".join(ligne)
                l.append(ligne)
            ligne=f.readline()
            k=k+1
        if choix ==0:
            print("le profil n'existe pas")
            print("Vous aller être rediriger vers le menu")
            time.sleep(5)
            return
    with open ("readers.txt","w") as f :
        for i in range (len(l)):
            f.write(l[i]+'\n')
#Cette partie modifie le fichier booksread.txt
    with open ("booksread.txt","r") as f :
        l=[]
        choix=0
        ligne=f.readline()
        k=0
        while ligne!="":
            ligne=ligne.rstrip()
            ligne=ligne.split(",")
            if pseudo != ligne[0]:
                ligne = ",".join(ligne)
                l.append(ligne)
            ligne=f.readline()

    with open("booksread.txt","w") as f :
        for i in range (len(l)):
            f.write(l[i]+'\n')
#Cette partie modifie la matrice de notatin dans le fichier matrice_note
    with open ("matrice_note","r")as f :
        l=[]
        cpt=0
        ligne=f.readline()
        while ligne!="":


            ligne = ligne.rstrip()
            l.append(ligne)
            ligne = f.readline()

    with open ("matrice_note","w") as f :
        cpt=0
        for i in range (len(l)):
            if cpt!=n:
                f.write(l[i]+'\n')
            cpt=cpt+1
    print("Le profil a été supprimer")
    print("Vous aller être rediriger vers le menu")
    time.sleep(5)

#--------------------------------------------------------------------------------------------------------------------
#Partie 2 --> Dépot de livre
#La fonction action_M2 donne accés a cette partie.

'''Cette fonction permet simplement d'afficher les livres.
Elle stocke les livres dans une lisyte avant de les afficher avec un indice.'''
def afficher_livre():
    print("----------          ----------")
    with open("books.txt", ) as book:
        l = []
        ligne = book.readline()
        i = 0
        while ligne != "":
            l.append(ligne)
            ligne = book.readline()
        for i in range(1, len(l) + 1):
            print(i, ".", l[i - 1])
        if i ==0:
            print("Il n'y a pas de livre")
            print("Vous allez être rediriger vers le menu")
            time.sleep(4)



'''Cette fonctio  permet d'ajouter un livre.'''
def ajouter_livre():
    print("----------          ----------")
    with open("books.txt", "r+") as f:
#Cette partie vérifie si le livre n'éxiste pas deja. Si Il n'existe pas le livre est ajouter dans le fichier books.txt
#Sinon l'utilisateur est redirigé vers le menu.
        livre = str(input("saisir le nom du livre a ajouter : "))
        ligne=f.readline()
        l=[]
        while ligne!="":
            l.append(ligne)
            if livre in ligne:
                print("le livre existe deja")
                print("Vous allez être renvoyé vers le menu.")
                time.sleep(5)
                return
            ligne=f.readline()
        if len(l) > 0:
            if "\n" not in l[len(l)-1]:
                f.write('\n')
        f.write(livre)
#Cette partie ajoute la colone du nouveau livre dans la matrice de notation.
    with open("matrice_note", "r") as f, open ("readers.txt","r") as f1 :
        M = []
        ligne = f1.readline()
        ligne1=f.readline()
        cpt=0
        while ligne != "":
            ligne1 = ligne1.rstrip()
            if ligne1=="":
                M.append(ligne1 + "0")
            else:
                M.append(ligne1 + " 0")
            ligne = f1.readline()
            ligne1 = f.readline()
            cpt=cpt+1
    with open("matrice_note", "w") as f:
        for i in range(len(M)):
            f.write(M[i])
            f.write('\n')
    print("Les modifications ont bien été apportées")



'''Cette fonction permert de modifié le nom d'un livre sans modifier les profils l'ayant lu ou ces notes dans la 
matrice de notation.'''
def modifier_livre():
    print("----------          ----------")
#Cette partie stock le fichier dans une liste avant de chercher le nom d'un livre fournit par l'utilisateur.
    with open("books.txt", "r") as f:
        choix = 0
        l = []
        ligne = "k"
        while choix == 0:
            if ligne == "":
                choix = 1
            else:
                ligne = f.readline()
                l.append(ligne)
        nom_livre = input("Saisir le nom du livre a modifier : ")
#Cette partie permet de rechercher le livre et de modifier son nom dans la liste avant de la réécrire dans le fichier.
        for i in range(len(l) - 1):
            if nom_livre in l[i]:
                l[i] = input("Saisir le nouveau nom du livre : ") + '\n'
                print("le livre a bien été modifié ")
                choix = 0
    with open("books.txt", "w") as f:
        for i in range(len(l) - 1):
            f.write(l[i])

    if choix == 1:
        print("Le livre n'existe pas ")
        print("Vous aller être rediriger vers le menu")
        time.sleep(5)



'''Cette fonctiojn permet de supprimer un livre des fichiers books.txt, booksread.txt et matrice_note'''
def supprimer_livre():
    print("----------          ----------")
#Cette partie stock le fichier books das une lisye avant de l'afficher avec un indice.
    print("Quels livres ne vous interresent plus ? :\n ")
    with open("books.txt", "r") as book:
        ligne = book.readlines()
        k = 1
        for i in ligne:
            print(k, ":", i)
            k += 1
#Cette partie permet a l'utilisateur de choisir quel livre supprimer et de confirmer son choix.
    x=-1
    if len(ligne)==0:
        print("Il n'y a pas de livre")
        print("Vous allez être rediriger vers le menu")
        time.sleep(4)
        return
    while x<=0 or x>len(ligne):
        x = int(input("Saisir le numéros du livre à supprimer  :\n "))
    y = str(x)

    print("Etes-vous sûr de vouloir supprimer", ligne[x - 1])
    verif = 0
    while verif < 1 or verif > 2:
        verif = int(input(' 1 - OUI \n 2 - NON \n Saisissez 1 pour confirmer la suppression ou 2 pour annuler: \n'))

    if verif == 1:
#Cette partir modifie les listes contenant les fichiers books et booksreads
        with open("books.txt", "r") as b, open("booksread.txt", "r") as br:
            ligne = b.readlines()
            copy = str()
            cpt = 1
            tab = []
            for i in ligne:
                if x != cpt:
                    tab.append(i)
                cpt += 1
            for i in tab:
                copy += i

            ligne1 = br.readline()
            copy1 = str()

            while ligne1 != "":
                k = ligne1.split(",")
                for i in range(len(k)):
                    k[i] = k[i].rstrip()

                tab1 = [k[0]]
                for i in range(1,len(k)):
                    if k[i] != y:
                        if int(k[i]) > x:
                            k[i] = int(k[i])-1
                        tab1.append(str(k[i]))
                    tab2=",".join(tab1)

                ligne1 = br.readline()
                copy1 += tab2+"\n"
#Cette partie réécrie les nouveaux fichiers.
        with open("books.txt", "w") as supp, open("booksread.txt", "w") as supp1:
            supp.write(copy)
            supp1.write(copy1)
        print("Le livre a bien été supprimer")
        print("Vous aller être rediriger vres le menu")
        time.sleep(5)
    else:
        print("Vous aller être rediriger vers le menu")
        time.sleep(5)
        return
#Cette partie supprime la colone associé au livre dans la matrice de notation
    with open("matrice_note", "r") as f:
        ligne = f.readline()
        l = []
        while ligne != "":
            ligne = ligne.rstrip()
            ligne = ligne.split(" ")
            l.append(ligne)
            ligne = f.readline()

        for i in range(len(l)):
            del l[i][x-1]

    with open("matrice_note", "w") as f:
        for i in range(len(l)):
            l[i] = " ".join(l[i])
            f.write(l[i])
            f.write('\n')



#----------------------------------------------------------------------------------------------------------------------
#Partie 3 --> recommandation
#La fonction action_M3 permet d'acceder a cette partie.



'''Cette fonction permet de noter des livres en modifiant la matrice de notation'''
def noter_livre() :
    print("----------          ----------")
#Cette partie verifie si le pseudo fournit par l'utilisateur existe.
    with open ("booksread.txt","r") as f :
        print("Quel est vorte pseudo ? ")
        pseudo=input("saisir votre pseudo : ")
        ligne=f.readline()
        utilisateur=""
        i=0
        while ligne!="":
            if pseudo in ligne :
                utilisateur=ligne
                n=i
            ligne=f.readline()
            i=i+1
        if utilisateur=="":
            print("Le profil n'existe pas")
            print("vous allez être rediriger vers le menu")
            time.sleep(5)
            return
#Cette partie stock le fichier books dans la liste l
    with open ("books.txt","r") as f :
        l=[]
        ligne=f.readline()
        a=1
        while ligne!="":
            ligne=ligne.rstrip()
            ligne=ligne.split(",")
            l.append(ligne)
            ligne=f.readline()
            a=a+1
    utilisateur=utilisateur.split(",")
#cette partie affiche les livres lu par l'utilisateur
    with open ("booksread.txt","r") as f :
        livre_lu=[]
        for i in range (len(utilisateur)):
            for j in range (1,len(l)+1):

                e=str(j)
                utilisateur[i]=utilisateur[i].rstrip()
                if utilisateur[i]==e:

                    print("vous avez lu : ",j,". ",l[j-1])
                    livre_lu.append(j)
    if len(livre_lu)==0:
        print("Vous n'avez pas lu de livre")
        print("Vous allez être rediriger vers le menu")
        time.sleep(4)
        return
#cette partie permet de noter les livres et de changer le fichier matrice_note
    with open ("matrice_note","r") as f :
        M=[]
        ligne = f.readline()
        while ligne!="":
            ligne=ligne.rstrip()
            ligne=ligne.split(" ")
            M.append(ligne)
            ligne = f.readline()
    print("combien de livre voulez vous noter ?")
    nb_livre_noter=int(input("Saisir nombre de livre : "))
    while nb_livre_noter <=0 or nb_livre_noter>len(livre_lu):
        nb_livre_noter = int(input("Saisir nombre de livre : "))
    for i in range (nb_livre_noter):
        print("Quel livre voulez vous modifier ?")
        livre=int(input("Saisir le numero du livre a noter : "))
        while livre not in livre_lu :
            livre = int(input("Saisir le numero du livre a noter : "))
        if M[n][livre-1]!=0:
            print("La note actuelle du livre est de ",M[n][livre-1])
        else:
            print("Vous n'avez pas encore donner de note au livre")
        print("Quelle note voulez vous donner au livre ")
        M[n][livre-1]=int(input("Saisir un chiffre en 1 et 5: "))
        while M[n][livre-1]<1 or M[n][livre-1]>5 :
            M[n][livre-1] = int(input("Saisir un chiffre en 1 et 5: "))
    with open ("matrice_note","w") as f :
        for i in range (len(M)):
            for j in range (a-1):
                M[i][j]=str(M[i][j])
            M[i]=" ".join(M[i])
            f.write(M[i])
            f.write('\n')
    print("Les modifications ont bien été apporter")
    print("Vous aller être rediriger vers le menu")
    time.sleep(5)
def similarité():
    with open ("matrice_note", 'r') as m :
        M=[]
        ligne=m.readline()
        while ligne != "" :
            L = ligne.split(" ")
            for i in range(len(L)):
                L[i] = L[i].rstrip()      #Pour commencer on transforme le ficher matrice_note en matrice qu'on stock dans M.
                L[i] = int(L[i])
            M.append(L)
            ligne= m.readline()

        F = []                           #On crée un matrice F qui va récupérer les résultats du calcules de similarité.
        for i in range(len(M)):
            k = i
            Solutions = []
            for i in range(len(M)):
                l1 = M[k]
                l2 = M[i]
                Numérateur = 0           #On calcule la similarité des lecteurs pour chaque chaque ligne de M 2 par 2.
                sommes1 = 0
                sommes2 = 0
                for i in range(len(l1)):            #Pour faciliter le calcule on le divise en petites étapes:
                    Numérateur += l1[i] * l2[i]      #On fait la sommes des produits des deux lignes.
                    sommes1 += l1[i]**2
                    sommes2 += l2[i]**2               #On sommes les carré de chaques éléments qui conposes la ligne.
                    racine1 = sqrt(sommes1)
                    racine2 = sqrt(sommes2)           #On calcule la racine de chaques sommes.
                    Dénominateur = racine1*racine2    #On conserve le produit des deux racine dans la variable Dénominateur.
                    if Dénominateur == 0:
                        Résultat = 0.00
                    else:
                        Résultat = round(Numérateur/Dénominateur,2)   #On divise la sommes des produits par le produit des carrés.
                Résultat2 = str(Résultat)             #On converti Résultat en str pour mieux le stocké après.
                Solutions.append(Résultat2)
            F.append(Solutions)

        texte = str()
        for i in F:
            l = i
            joindre = ' '.join(l)                  #Ici on transforme F en texte qu'on copie dans notre fichier.
            texte += joindre + '\n'

    with open("similarité.txt", "w") as m :
        m.write(texte)

    return F         #On retourn F pour l'utiliser.

def suggérer_livre():
    print("----------          ----------")
    with open("booksread.txt", 'r') as br, open("readers.txt") as r, open("books.txt", "r") as b:
        ligne = r.readline()
        tableu_useur = []
        k = 1
        while ligne != "":
            ligne = ligne.split(",")
            tableu_useur.append(ligne[0])      #Etape pour afficher la liste des lecteurs
            print(k, ":", ligne[0])
            ligne = r.readline()
            k += 1

        x = -1
        ligne1 = r.readlines()
        while x<=0 or x>k-1:
            x = int(input("Saisir le numéros du lecteur à étudier:\n "))

        print("Souhaitez-vous être affilié à un autre lecteur ?")
        z = -1
        print(" 1 - OUI \n 2 - NON")
        while z < 1 or z > 2:
            z = int(input("Saisissez le numéro correspondant à votre choix:\n"))

        if z==1 :                          #Si le lecteur souhaite être affilié à un autre lecteur:
            F = similarité()
            l=[]                      #On crée un liste correspondant à sa ligne de similarité.
            max=0
            for i in range(len(F)):
                if i == x - 1:
                    l.append(0)
                else:
                    l.append(F[x - 1][i])

            for i in range(len(l)):
                y=float(l[i])
                if y > max:               #A cette liste on fait parcourire un max qui prend la valeur max de la liste.
                    max = y               #k = l'indice de ce lecteur
                    k = i
            if max != 0:
                print("Vous êtes compatible à", floor(max * 100), "%", "avec le lecteur", tableu_useur[k].rstrip())
                lecteurs = br.readlines()
                lecteur_c = lecteurs[k].split(",")    #on crée un liste qui contient les livres lu par le lecteur compatible.
                lecteur_p = lecteurs[x - 1].split(",") #on crée un liste qui contient les livres lu par le lecteur principale.
                for i in range(len(lecteur_p)):
                    lecteur_p[i] = lecteur_p[i].rstrip()
                for i in range(len(lecteur_c)):
                    lecteur_c[i] = lecteur_c[i].rstrip()

                livres_non_lu = []
                for i in range(1, len(lecteur_c)):
                    if lecteur_c[i] not in lecteur_p:  #On cherche les livres que le lecteur Principale n'as pas lu.
                        livres_non_lu.append(lecteur_c[i])  #Ils sont stocké dans "livres_non_lu".

                print("Veuillez patienter, une liste de livre qui pourrais vous correspondre va bientôt s'afficher:\n")
                time.sleep(4)

                if len(livres_non_lu) == 0:
                    print("Malheureseument, le lecteur", tableu_useur[k].rstrip(), "et vous avez lu les mêmes livres")
                    print("Essayer avec un autre lecteur la prochaine fois\n")
                    print("Vous aller être rediriger vers le menu")
                    time.sleep(4)
                    return

                else:
                    books = b.readlines()
                    cpt = 1
                    for i in livres_non_lu:
                        print(cpt, ":", books[int(i) - 1].rstrip())
                        cpt += 1           #On lui affiche la liste des livres qui sont suceptible de lui plaire (càd qu'il n'a pas lu).
                    print("\nSouhitez-vous ajouter un de ces livres à votre bibliothèque ?")
                    print(" 1 - OUI \n 2 - NON ")
                    choix = 0
                    while choix < 1 or choix > 2:
                        choix = int(input("Saisissez le numéro correspondant à votre choix:\n"))

                    if choix == 1:
                        c = -1
                        while c < 0 or c > len(livres_non_lu):
                            c = int(input("Veuiller saisir le numéro du livre à ajouter:\n"))

                        livre_à_ajouter = livres_non_lu[c - 1]  #on ajoute le livre que le lecteur à choisi dans "livre_à_ajouter".
                        lecteur_p.append(livre_à_ajouter)       #Qu'on ajoute ensuite dans le listes des livre lu par le lecteur principale.

                        texte = ",".join(lecteur_p)
                        copy = str()
                        for i in range(len(lecteurs)):
                            if i == x - 1:
                                copy += texte + "\n"              #on convertie la liste des livres lu par le lecteur en str dans copy
                            else:
                                copy += lecteurs[i]

                        with open("booksread.txt", "w") as modf:         #On modifie le fichier contenant tout les livres lu
                            modf.write(copy)                              #par chaque lecteurs en prenant soin d'y ajouter copy.

                        print("le livre à bien été ajouter\n")
                        print("Souhaitez-vous lui attribuer une note ?")
                        print(" 1 - OUI \n 2 - NON ")
                        choix = 0
                        while choix < 1 or choix > 2:
                            choix = int(input("Saisissez le numéro correspondant à votre choix:\n"))

                        if choix == 1:
                            print("Vous aller être rediriger vers le système de notation")
                            time.sleep(4)
                            noter_livre()

                        else:
                            print("Vous aller être rediriger vers le menu")
                            print("N'oubliez pas de noter le livre un fois l'avoir lu ! ")
                            time.sleep(4)
                            return

                    else:
                        print("Dommage, vous aller être rediriger vers le menu")
                        time.sleep(4)
                        return

            else:
                print("Malheuresement vous n'êtes compatible avec aucun lecteur\n")
                print("Vous aller être rediriger vers le menu")
                time.sleep(4)
                return

        else:
            print("Vous aller être rediriger vers le menu")
            time.sleep(4)
            return