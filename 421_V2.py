# on met les dé en aléatoire
from random import *
def dé1():
  dé1=randint(1,6)
def dé2():
  dé2=randint(1,6)
def dé3():
  dé3=randint(1,6)
def jeu(dé1,dé2,d3):
  # on affiche les trois dé
  print(dé1,dé2,dé3)
# on aditionne les trois dé car on a compris que si le total est égal à sept alors les trois dés feront quatre cent vingt et un 
  total=dé1+dé2+dé3
  for i in range (3): 
    if total==7
      if dé1==4 or dé2==4 or dé3==4:
        print("vous avez gangné !")
      else:
        print("réesseyer ")
    else:
      print("réesseyer")
print("1er joueur")
jeu(dé1(),dé2(),dé3())
print("2ème joueur")
jeu(dé1(),dé2(),dé3())
