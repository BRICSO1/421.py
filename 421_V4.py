# on met les dé en aléatoire
from random import *
from time import *
charge=21
player1_name=input('premier joueur : ')
player2_name=input('deuxième joueur : ')
# intialistaion des joueurs gain potentiel
player1_jeton=0
player2_jeton=0
# intaltion des jetons pour les joueurs total
player1_total=0
player2_total=0
# sert pour désigner les joueurs impair=permier joueur et pair= deuxième joueur
playing=1
while charge!=0 or charge<=0:
    dé1=randint(1,6)
    dé2=randint(1,6)
    dé3=randint(1,6)
    # tri des nombre du plus petit au plus grand
    print(dé1,dé2,dé3)
    player1_jeton=0
    player2_jeton=0
    total=dé1+dé2+dé3 
    if playing%2!=0 :
        if total==7 and (dé1==4 or dé2==4 or dé3==4):
            print("421 ",player1_name," prenez 10 jetons")
            charge=charge-10
            player1_jeton=player1_jeton+10
            # règle des trois as 
        elif dé1==1 and dé2==1 and dé3==1:
            player1_jeton=player1_jeton+7
            print(player1_name," a gagnez 7 jetons")
        elif total==8 and (dé1==6 or dé2==6 or dé3==6):
            player1_jeton=player1_jeton+6
            print(player1_name," a gagné 6 jetons")
        elif total==18:
            player1_jeton=player1_jeton+6
            print("vous avez gagné 6 jetons") 
        elif total==7 and (dé1==5 or dé2==5 or dé3==5):
            player1_jeton=player1_jeton+6
            print(player1_name," a gagné 5 jeton")
        elif dé1==5 and dé2==5 and dé3==5:
            player1_jeton=player1_jeton+5
            print(player1_name," a gagné 5 jetons")
        elif total==6 and (dé1==4 or dé2==4 or dé3==4) and(dé1==2 or dé2==2 or dé3==2):
            player1_jeton=player1_jeton+4
            print(player1_name,' a gagné 4 jeton')
        elif dé1==4 and dé2==4 and dé3==4:
            player1_jeton=player1_jeton+4
            print(player1_name,' a gagné 4 jetons')
        elif total==5 and (dé1==3 or dé2==3 or dé3==3):
            player1_jeton=player1_jeton+3
            print(player1_name,' a gangné 3 jetons')
        elif dé1==3 and dé2==3 and dé3==3:
            player1_jeton=player1_jeton+3
            print(player1_name," a gagné 3 jetons")
        elif total==4 and (dé1==2 or dé2==2 or dé3==2):
            player1_jeton=player1_jeton+2
            print(player1_name,' a  gagnez 2 jetons')
        elif dé1==2 and dé2==2 and dé3==2:
            player1_jeton=player1_jeton+2
            print(player1_name," a  gagné 2 jetons")
        else:
            print(player1_name,' a gagné 1 jeton')
            charge=charge-1
            player1_jeton=player1_jeton+1
        print(player1_name,' a ', player1_jeton)
        if charge<=0:
            break
        playing=playing+1
        sleep(0.5)
            
    else:
        if total==7 and (dé1==4 or dé2==4 or dé3==4):
            print("421", player2_name,"prenez 10 jetons")
            player2_jeton=player2_jeton+10
            # règle des trois as 
        elif dé1==1 and dé2==1 and dé3==1:
            player2_jeton=player2_jeton+7
            print(player2_name," a 7 jetons")
        elif total==8 and (dé1==6 or dé2==6 or dé3==6):
            player2_jeton=player2_jeton+6
            print(player2_name," a gagné 6 jetons")
        elif total==18:
            player2_jeton=player2_jeton+6
            print(player2_name," a gagné 6 jetons") 
        elif total==7 and (dé1==5 or dé2==5 or dé3==5):
            player2_jeton=player2_jeton+6
            print(player2_name," a gangné 5 jeton")
        elif dé1==5 and dé2==5 and dé3==5:
            player2_jeton=player2_jeton+5
            print(player2_name,' a gagné 5 jetons')
        elif total==6 and (dé1==4 or dé2==4 or dé3==4) and(dé1==2 or dé2==2 or dé3==2):
            charge=charge-4
            player2_jeton=player2_jeton+4
            print(player2_name,' a gagné 4 jeton')
        elif dé1==4 and dé2==4 and dé3==4:
            player2_jeton=player2_jeton+4
            print(player2_name,' a gagné 4 jetons')
        elif total==5 and (dé1==3 or dé2==3 or dé3==3):
            player2_jeton=player2_jeton+3
            print(player2_name,' a gangné 3 jetons')
        elif dé1==3 and dé2==3 and dé3==3:
            player2_jeton=player2_jeton+3
            print(player2_name,' a gagné 3 jetons')
        elif total==4 and (dé1==2 or dé2==2 or dé3==2):
            player2_jeton=player2_jeton+2
            print(player2_name,' a gagnez 2 jetons')
        elif dé1==2 and dé2==2 and dé3==2:
            player2_jeton=player2_jeton+2
            print(player2_name," a gagné 2 jetons")
        else:
            print(player2_name,' a gagné 1 jeton')
            player2_jeton=player2_jeton+1
        print(player2_name,' a ', player2_jeton)
        if charge<=0:
            break
        playing=playing+1
        sleep(0.5)
    if player1_jeton>player2_jeton:
        charge=charge-player1_jeton
        player1_total=player1_total+player1_jeton
        print(player1_name,' gagne les jetons')
        print(" ")
    elif player1_jeton<player2_jeton:
        charge=charge-player2_jeton
        player2_total=player2_total+player2_jeton    
        print(player2_name,' a gagné les jetons')
        print(' ')
    else :
        # saut de ligne
        print("annulé")
        print(' ')
if charge!=0:
    print("le jeu est terminé")
elif player1_total<player2_total:
    print("Bravo, le joueur 1 a gagné")
else:
    print("Bravo, le joueur 2 a gagné")
    
print(player1_name, "a ", player1_total, " et ", player2_name, " a ", player2_total)