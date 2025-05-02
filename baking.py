import time
import sys
import random
import curses
from progress.bar import FillingSquaresBar

food_targets = ["Cupcakes", "Chocolate Cake", "Pancakes", "Exit"]
ingredients = ["Flour", "Eggs", "Butter", "Milk", "Vanilla Extract", "Sugar", "Baking Powder", "Salt"]
wet = ["Eggs", "Butter", "Milk", "Vanilla Extract"]
dry = ["Flour", "Sugar", "Baking Powder", "Salt"]
# main loop
stop = False
while not stop:
    print("Time to bake!")
    for number, food in enumerate(food_targets):
        print(f"{number+1}) {food}")
    try:
        bakechoice = int(input("> "))
    except:
        print("That's not a good number! Try again.\n")
        continue
    if bakechoice < 1 or bakechoice > len(food_targets):
        print("That's not a good number! Try again.\n")
        continue

    if bakechoice == len(food_targets):
        print("Goodbye!")
        stop = True
        continue

    if bakechoice == 1:
        '''
        this_ingredients = ingredients + ["Oil"]
        this_wet = wet + ["Oil"]
        this_dry = dry
        user_wet = []
        user_dry = []
        random.shuffle(this_ingredients)
        print("Sort the ingredients into wet and dry!")
        for ingredient in this_ingredients:
            while True:
                print("Type 1 for wet, 2 for dry")
                print(f"{ingredient}: ", end="")
                try:
                    choice = int(input("> "))
                except:
                    print("That's not a good number! Try again.\n")
                    continue
                if choice == 1:
                    user_wet.append(ingredient)
                    break
                elif choice == 2:
                    user_dry.append(ingredient)
                    break
                else:
                    print("That's not a good number! Try again.\n")
                    continue
        incorrect = 0
        for ingredient in this_ingredients:
            if ingredient in this_wet and ingredient not in user_wet:
                print(f"Oops! You forgot to add {ingredient} to the wet ingredients.")
                incorrect +=1
            elif ingredient in this_dry and ingredient not in user_dry:
                print(f"Oops! You forgot to add {ingredient} to the dry ingredients.")
                incorrect +=1
        if incorrect >= 1:
            print(f"you got {incorrect} wrong!")
            sys.exit(1)
        else:
            print("Great job! You sorted the ingredients!")'''

        print("Time to mix them together!!!")
        mixing_times = 1#random.randint(2, 5)
        for mixing_iter in range(mixing_times):
            print("Order these numbers from least to greatest!")
            print("Seperate them with spaces")

            mixing_numbers = []
            for i in range(5):
                num = random.randint(0, 100)
                while num in mixing_numbers:
                    num = random.randint(0, 100)
                mixing_numbers.append(num)

            random.shuffle(mixing_numbers)
            print(mixing_numbers)

            user_sort = input("\n> ")
            user_sort_list_str = user_sort.split(" ")
            user_sort_list = []

            for i in user_sort_list_str:
                user_sort_list.append(int(i))

            mixing_numbers.sort()
            # ALERT THIS IS CHEATING
            #
            #
            user_sort_list = mixing_numbers
            #
            #
            #
            if mixing_numbers != user_sort_list:
                print("You sorted wrong and the whisk exploded :(")
                sys.exit(1)
            else:
                print(f"Great job! Only {mixing_times-(mixing_iter+1)} more to go!")
        
        print("Now we have to bake it for a certain amount of time!")
        going_up = True
        bar_value = 0
        stop_bar = False

        print("Press space when the bar is almost filled")
        print("Get ready!")
        time.sleep(3)

        stdscr = curses.initscr()
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        stdscr.nodelay(True)

        try:
            with FillingSquaresBar("Baking", max=100) as bar:
                while not stop_bar:

                    key = stdscr.getch()
                    if key == ord(' '):
                        stop_bar = True
                        break

                    if going_up:
                        bar_value += 2
                        if bar_value >= 100:
                            going_up = False
                    else:
                        bar_value -= 2
                        if bar_value <= 0:
                            going_up = True

                    bar.goto(bar_value)
                    time.sleep(0.05)
        finally:
            curses.nocbreak()
            curses.echo()
            curses.endwin()

        

        sys.stdout.flush()
        print(bar_value)
        
