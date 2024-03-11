import random
game = True
yazi = 0 
tura = 0

while game:
  rastgele = random.randint(0,1)
  if rastgele == 0:
    print("Tura!\n")
    tura += 1
  else:
    print("Yazı!\n")
    yazi += 1
  print("Yazı: ", yazi, "\nTura: ", tura ,"\n")
  user = input("do u wanna play again? (type 'y' or 'n')")
  if user == "n":
    game = False
  