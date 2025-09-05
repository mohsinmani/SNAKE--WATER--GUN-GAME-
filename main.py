'''
1 for snake
-1 for water
0 for gun

'''
# import random

# computer = random.randrange(-1 , 2)

# youstr = input("Enter your choice: ")
# yourDict = {
#             "s": 1,
#             "w": -1,
#             "g": 0
#             }
# you = yourDict[youstr]

# if(computer == -1 and you == 1):
#     print("You win!")
# elif(computer == -1 and you == 0):
#     print("You lose!")
# elif(computer == 1 and you == -1):
#     print("You lose!")
# elif(computer == 1 and you == 0):
#     print("You win!")
# elif(computer == 0 and you == -1):
#     print("You win!")
# elif(computer == 0 and you == 1):
#     print("You lose!")
# else:
#     print("Something went wrong!")

import random

# 1 = Snake, -1 = Water, 0 = Gun
yourDict = {
            "s": 1,
            "w": -1,
            "g": 0
            }

reverseDict = {
                1: "Snake",
               -1: "Water",
                0: "Gun"
              }

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

if youstr not in yourDict:
    print("Invalid choice!")
else:
    you = yourDict[youstr]

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    if (computer == you):
        print("It's a draw!")
    elif (computer == 1 and you == -1):   # Snake vs Water
        print("You lose! Snake drinks water.")
    elif (computer == -1 and you == 0):   # Water vs Gun
        print("You lose! Water douses gun.")
    elif (computer == 0 and you == 1):    # Gun vs Snake
        print("You lose! Gun shoots snake.")
    elif (you == 1 and computer == -1):
        print("You win! Snake drinks water.")
    elif (you == -1 and computer == 0):
        print("You win! Water douses gun.")
    elif (you == 0 and computer == 1):
        print("You win! Gun shoots snake.")
    else:
        print("Something went wrong!")

