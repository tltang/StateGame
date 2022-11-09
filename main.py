import turtle
import pandas
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
score = Scoreboard()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
lAnswer = True
guess_list = []
missed_state = []

while lAnswer or score.score_total < 50:
    answer_state = screen.textinput(title=f"{score.score_total} / {len(data)} States Correct", prompt="What's another state's name?")
    selected_state = data[data["state"].str.lower() == answer_state.lower()]

    if answer_state == 'Exit':
        missed_state = [state for state in data.state if state not in guess_list]
        break

    if selected_state.empty:
        lAnswer = False
    else:
        guess_list.append(answer_state)
        x = selected_state["x"]
        y = selected_state["y"]
        coor = (int(x), int(y))
        score.score()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(coor)
        t.pendown()
        t.write(answer_state)


df = pandas.DataFrame(missed_state)
df.to_csv("missed_state.csv")


screen.exitonclick()