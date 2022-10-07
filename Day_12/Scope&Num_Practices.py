################### Scope ####################

# enemies = 1
#
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# ******Local Scope
# def drink_potion():
#     potion_st = 2
#     print(potion_st)
#
# drink_potion()
# print(potion_st) # error because of the local scope

# ******Global Scope

player_health = 10
def game():
    def drink_potion():
        print(player_health) # player_health is assemble because it is defined in the global level

    drink_potion() # function can be nested too *****
print(player_health)

#*********There is no Block Scope in python

game_level = 3
enemies = {"Skeleton", "Zombie", "Alien"}

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # new element created inside the if block will able to access outside the if block but not in the functions so


# *********** Modifying the Global Scope
# do not create the global and local variable with same name
enemies = 1
# To use global V inside the function we have to redefine the V inside again as glbal
def increase_enemies():
    # global enemies
    enemies_l = 0
    enemies_l += enemies + 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# ********* Global Constants  V which we define and never want to change that again
# ********* Use all the global V as UPPER CASE

PI = 3.14159
URL = "https://www.google.com"



