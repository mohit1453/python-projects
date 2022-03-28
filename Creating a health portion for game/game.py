import random
health=50
print("Please Enter Your Difficulty Level 1 ,2 ,3: ? ")
level=int(input())
portion_health=int(random.randint(20,50)/level)
health=health+portion_health
print("Player level is " +str(level) +" And Your health is " +str(portion_health))
