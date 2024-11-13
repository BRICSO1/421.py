# on met les dé en aléatoire
from random import *
dé1=randint(1,6)
dé2=randint(1,6)
dé3=randint(1,6)

# on affiche les trois dé
print(dé1,dé2,dé3)
# on aditionne les trois dé car on a compris que si le total est égal à sept alors les trois dés feront quatre cent vingt et un 
total=dé1+dé2+dé3 
if total==7:
  if dé1==4 or dé2==4 or dé3==4:
    print("vous avez gagné !")
# règle des trois as 
elif dé1==1 and dé2==1 and dé3==1:
  print("vous avez gagné !")
else:
  print("réessayez")
