from turtle import Turtle,Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)


# myscreen = Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()



table = PrettyTable()

# table.field_names = ["Name", "Age"]
# table.add_row(["Arnav", 20])
# table.add_row(["Angela", 35])

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire",])

table.align = 'l'

print(table)