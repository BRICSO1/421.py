from random import *
def dé1():
  dé1=randint(1,6)
def dé2():
  dé2=randint(1,6)
def dé3():
  dé3=randint(1,6)
print(dé1(),dé2(),dé3())
total=dé1+dé2+dé3
if total==7:
  if dé1()==4 or dé2()==4 or dé3()==4 :
    print("vous avez gangné !")
  else:
    print("réesseyer ")