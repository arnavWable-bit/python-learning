# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Local scope

# def drint_potion():
#     potion_strength = 2
#     print(potion_strength)

# drint_potion()
# print(potion_strength)                       # this gives error because potion strength is a local variable



# Global scope

# player_health = 10
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()

# game()



# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)



# game_level = 10
# enemies = ["Skeleton", "Zombie", "Alien"]

# def game():
#     new_enemy = ""
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)



# Modifying global scope

enemies = 1

def increase_enemies(enemy):
    #global enemies                        # You can but it is recommended not to modify global scope
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

