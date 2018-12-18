import random

numberofGuesses = 0
number = random.randint(1,98)
Aiden = {"Ce programme Ã  Ã©tait dÃ©velopper par [Dev]Aiden24"}

name = raw_input("Bonjour quel est ton nom ? ")

print("Je pense aÂ  un nombre entier entre 1 et 98. Pouvez-vous deviner ce que c'est ? ")
raw_input ("Etes vous prÃªt ?")
raw_input("Bon jeu ! ;)")
print("Ce programme Ã  Ã©tait dÃ©velopper par [Dev]Aiden24")

while numberofGuesses < 98:
  guess = raw_input("Devinez le nombre")
  guess = int(guess)

  numberofGuesses = numberofGuesses + 1;
  guessesLeft = 98 - numberofGuesses;

  if guess < number:
    guessesLeft=str(guessesLeft)
    print("Taproposition est trop basse! Tu a " + guessesLeft + " essaie")
    guessLeft=str(guess)
    print("Entre un autre chiffre !")

  if guess > number:
    guessesLeft=str(guessesLeft)
    print("Ta proposition est trop Haute ! Tu a " + guessesLeft + " essaie")
    guessLeft=str(number)
    print("Entre un autre chiffre !")

  if guess==number:
    break

if guess==number:
  numberofGuesses=str(numberofGuesses)
  print("Bon travail! Tu Ã  deviner le nombre en " + numberofGuesses + " fois :)")

if guess!=number:
  number=str(number)
  print("Pardon. Le nombre auquel je pensais etait " + number + " :)")

