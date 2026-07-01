import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "day-25/US States project/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# Helps getting coordinates of states 
# def get_mouse_click_coor(x,y):
#     print(x,y)
    
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# data = pd.read_csv("day-25/US States project/50_states.csv")

# # score = 0
# guessed_states = []
# writer = turtle.Turtle()
# writer.hideturtle()
# writer.penup()
# all_states = data.state.to_list()
# missing_states = []

# while len(guessed_states) < 50 :
#     answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()
#     state_data = data[data["state"] == answer_state]
#     if not state_data.empty:
#         if answer_state not in guessed_states:
#             guessed_states.append(answer_state)
#             # score += 1
#             X = state_data.x.iloc[0]
#             Y = state_data.y.iloc[0]
#             writer.goto(x=X, y=Y)
#             writer.write(answer_state)

#     if answer_state == "Exit":
#         game_is_over = True
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         df = pd.DataFrame(missing_states)
#         df.to_csv("day-25/US States project/states_to_learn.csv",index=False)
#         break






# ANGELA's METHOD
# data = pd.read_csv("day-25/US States project/50_states.csv")


# guessed_states = []
# writer = turtle.Turtle()
# writer.hideturtle()
# writer.penup()
# all_states = data.state.to_list()

# while len(guessed_states) < 50 :
#     answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()
#     if answer_state == 'Exit':
#         missing_states = []
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pd.DataFrame(missing_states)
#         new_data.to_csv("States_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(state_data.x.item(), state_data.y.item())
#         t.write(answer_state)




# Modifying using List Comprehension
data = pd.read_csv("day-25/US States project/50_states.csv")


guessed_states = []
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
all_states = data.state.to_list()

while len(guessed_states) < 50 :
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


# screen.exitonclick()
