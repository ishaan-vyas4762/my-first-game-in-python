import random
def eggsnatcher():
    score=0
animals=["python","fox","monkey"]
rounds=5 
score=0

print("welcome to the amazing game made by Ishaan Vyas, this game is called egg snatcher in this there are 3 sneaky animals and in each round you have to guess who has stolen the egg, so what are you waiting for now play the game and enjoy!!!!")

for i in range(1,rounds+1):
    animals_with_egg = random.choice(animals)
    print(" round{}: choose an animal youre suspicious of from (python,fox,monkey):".format(i))
    guess=input("your guess:")

    if guess not in animals:
        print("Wow, you are DUMB, even a lkg kid could guess from the list of THREE above")
        continue
    if guess == animals_with_egg:
        print("great! now you can make an delicious egg fry to eat and you can even eat",format(animals_with_egg),"if you want to")
        score += 1
        
    else:
        print("wrong! now you cant make an egg fry and ",format(animals_with_egg),"(who stole the egg) also can come AGAIN")
print(score)

if score == 5:
    print("congratulations! you have earned the SIGMA EGG, now you are a true GEN Z")
else:
    print("play again for another mystery egg")
    
if score == 3:
    print("congratulations! you have earned the THUNDER EGG, now you can party with THOR and LOKI")

elif score == 0:
    print("oh noo! you have earned the CURSED EGG, if you want to break the curse replay the game")

elif score == 1:
    print("great! now you'll finally get a FROOTI from meenu maam")

elif score == 2:
    print("lucky you! you just earned MONEY EGG, you have a money luck for 24 hours $$$$$$$$$$$")

elif score == 4:
    print("nice job! you got MEMORY EGG, it will help you increase your memory")

print("it also have more of the egg achievements, if you want to collect all of achievements play again and have fun!!") 
print("thank you for playing our game please write a comment for us to how to improve on this")
x=(input("comment:"))
print("thank you")
    
if "name"=="main":
    eggsnatcher()
     






        
        
        
          
    





