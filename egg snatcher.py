import random
def eggsnatcher():
    score=0
animals=["python","fox","monkey"]
rounds=5 #number of rounds to play
score=0

print("welcome to the amazing game made by Ishaan Vyas and Aditya Walia this game is called egg snatcher in this there are 3 naughty animals and in each round you have to guess who has stolen the egg now play the game and enjoy!")
for i in range(1,rounds+1):
    #randomly select the animal having egg
    animals_with_egg = random.choice(animals)
    print(" round{}: choose an animal youre suspicious of from (python,fox,monkey):".format(i))
    guess=input("your guess:")

    if guess not in animals:
        print("Wow, you are DUMB, even a lkg kid could guess from the list of THREE above")
        continue #skip this round
    if guess == animals_with_egg:
        print("great! now you can make an delicious egg fry to eat and you can even eat",format(animals_with_egg),"if you want to")
        score += 1
        
    else:
        print("wrong! now you cant make an egg fry and ",format(animals_with_egg),"(who stole the egg) also can come AGAIN")
print(score)
print("Game over! your score is.",score," [there is an easter egg too in which you can get a mystery egg on getting all 5 rounds correct and one on getting 3 rounds correct]")
#check for baby gronk egg
if score == 5:
    print("congratulations! you have earned the BABY GRONK EGG, now you are a true SKIBBIDI")
else:
    print("play again for another mystery egg")
#check for thunder egg
if score =< 3:
    print("congratulations! you have earned the THUNDER EGG, now you can party with THOR and LOKI")

print("thank you for playing our game please write a comment for us to how to improve on this")
x=(input("comment:"))
print("thank you")
    
if "_name_"=="_main_":
    eggsnatcher()
     






        
        
        
          
    





