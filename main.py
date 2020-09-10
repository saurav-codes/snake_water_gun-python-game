# ================ SNAKE - WATER - GUN ============================
# snake water gun
import random


def gamer_choose_snake():
    print("you had choosed Snake")
    print("Please wait ! computer is thinking..........!")
    comp_choice = random.choice(pc_choice_rand)
    if comp_choice == "snake":
        print("DRAW ! Snake can't fight with Snake")
    elif comp_choice == "water":
        print("YOU WIN !.. snake drinked the water")
    elif comp_choice == "gun":
        print("YOU LOOSE ! computer killed your snake by his Gun")

pc_choice_rand = ["snake","water","gun"]
print("==================== [[ SNAKE - WATER - GUN ]] =======================")
usr_choice = input(str("you have 3 choices available......\n==> press s for snake\n==> press w for water\n==> press g for gun\n==> press e for exit the game and show score\n==> press r to start the game\n"))
while usr_choice != "e":
    gamer_choice = str(input(("select your choice between snake,water & gun or press e to exit the game\n")))
    if gamer_choice=="s":
        gamer_choose_snake()
    elif gamer_choice=="w" :
        pass
    elif gamer_choice=="g":
        pass
    elif gamer_choice=="e" or gamer_choice=="E":
        ex_conf = str(input(("you choosed to exit the game.! Are you sure you want to exit\npress y for yes and n for continue playing...")))
        if ex_conf == "n":
            continue
        else:
            print("exiting the game..")
            exit()
    else:
        print("Please choose between the provided options only")

