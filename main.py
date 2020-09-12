# ================ SNAKE - WATER - GUN ============================
# snake water gun
import random
import time


initial_time = time.time()

pc_choice_rand = ["snake","water","gun"]
def gamer_choose_snake():
    global score
    global comp_score
    print("you had choosed Snake 🐍")
    print("Please wait ! computer is thinking..........!")
    time.sleep(1)
    comp_choice = random.choice(pc_choice_rand)
    if comp_choice == "snake":
        print("DRAW ! Snake can't fight with Snake")
        score = score+0
        comp_score = comp_score+0
        print("Your score🙋 is ",score)
        print("The score🙋 of computer is :",comp_score)
    elif comp_choice == "water":
        print("YOU WIN !.. snake drinked the water")
        score = score+5
        comp_score = comp_score-1
        print("Your score🙋 is ",score)
        print("The score🙋 of computer is :",comp_score)
    elif comp_choice == "gun":
        print("YOU LOOSE ! computer killed your snake by his Gun")
        score = score-1
        comp_score = comp_score+5
        print("Your score🙋 is",score)
        print("The score🙋 of computer is :",comp_score)
def gamer_choose_water():
    global score
    global comp_score
    print("you had choosed Water 🌊")
    print("Please wait ! computer is thinking..........!")
    time.sleep(1)
    comp_choice = random.choice(pc_choice_rand)
    if comp_choice == "snake":
        print("YOU LOSE!.. snake drinked the water")
        score = score-1
        comp_score = comp_score+5
        print("Your score🙋 is",score)
        print("The score🙋 of computer is :",comp_score)
    elif comp_choice == "water":
        print("DRAW ! Water can't fight with Water")
        score = score+0
        comp_score = comp_score+0
        print("Your score🙋 is",score)
        print("The score🙋 of computer is :",comp_score)
    elif comp_choice == "gun":
        print("YOU WIN ! you destroyed the computer's Gun")
        score = score+5
        comp_score = comp_score-1
        print("Your score🙋 is",score)
        print("The score🙋 of computer is :",comp_score)
def gamer_choose_gun():
    global score
    global comp_score
    print("you had choosed Gun 🔫")
    print("Please wait ! computer is thinking..........!")
    time.sleep(1)
    comp_choice = random.choice(pc_choice_rand)
    if comp_choice == "snake":
        print("YOU WIN ! you killed computer's snake by Gun ")
        score = score+5
        comp_score = comp_score-1
        print("Your score🙋 is",score)
        print("The score🙋 of computer is :",comp_score)
    elif comp_choice == "water":
        print("YOU LOSE !.. computer's water wiped your gun away")
        score = score-1
        comp_score = comp_score+5
        print("Your score🙋 is",score)
        print("The score🙋 of computer is :",comp_score)
    elif comp_choice == "gun":
        print("DRAW ! Gun can't fight with Gun")
        score = score+0
        comp_score = comp_score+0
        print("Your score🙋 is",score)
        print("The score🙋 of computer is :",comp_score)


# Main program here :

print("==================== [[ SNAKE - WATER - GUN ]] =======================")
usr_choice = input(str("you have 3 choices available......\n==> press s for snake 🐍\n==> press w for water🌊\n==> press g for gun🔫\n==> press e for exit⏱ the game and show score\n==> press any key to start the game\n"))
score = 0
comp_score = 0
while usr_choice != "e":
    gamer_choice = str(input(("\nselect your choice between snake,water & gun or press e to exit the game\n")))
    if gamer_choice=="s":
        gamer_choose_snake()
    elif gamer_choice=="w" :
        gamer_choose_water()
    elif gamer_choice=="g":
        gamer_choose_gun()
    elif gamer_choice=="e" or gamer_choice=="E":
        ex_conf = str(input(("you choosed to exit the game.! Are you sure you want to exit\npress y for yes and n for continue playing...")))
        if ex_conf == "n":
            continue
        else:
            print("\n🐻__Thanks for your time__🐻")
            time.sleep(1)
            print("\nYour score 🙌 is :",score,"      computer score 🙌 is :",comp_score)
            if score<comp_score:
                print("The computer defeated you by ",comp_score - score,"points")
            else:
                print("You defeated the computer by",score - comp_score,"points")
            sec_initial = time.time()
            print("You have played this game🐻 for..",sec_initial-initial_time,"seconds⏱")
            print("\nexiting the game..⏱\n")
            time.sleep(1)
            exit()
    else:
        print("Please choose between the provided options only 😕")

else:
    print("\n🐻__Thanks for your time__🐻\n\nYour score 🙌 is :",score,"\nexiting the game.....⏱\n")
    sec_initial = time.time()
    print("You have played this game🐻 for..",sec_initial-initial_time,"seconds⏱")