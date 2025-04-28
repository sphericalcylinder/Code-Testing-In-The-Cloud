import time
import random

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
        this_ingredients = ingredients + ["Oil"]
        this_wet = wet + ["Oil"]
        this_dry = dry
        user_wet = []
        user_dry = []
        random.shuffle(this_ingredients)
        print("Sort the ingredients into wet (1) and dry (2)!")
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
                elif choice == 2:
                    user_dry.append(ingredient)
                else:
                    print("That's not a good number! Try again.\n")
                    continue
