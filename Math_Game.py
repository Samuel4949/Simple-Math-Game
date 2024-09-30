import turtle as trtl
import random as rand

print("Welcome to a Math Game: Help the Wizard defend the Forest \nWhat Difficulty Would You Like?")
mode = input("Easy, Medium, or Hard? ")
while mode not in ["Easy", "Medium", "Hard"]:
  print("Type one of the following: Easy, Medium, Hard")
  mode = input("Medium, Hard? ")
  if mode in ["Easy", "Medium", "Hard"]:
    break

wn = trtl.Screen()
wn.setup(600, 600)
wn.bgpic("Forest.gif")

avatar_image = "Wizard.gif"
wn.addshape(avatar_image)
avatar = trtl.Turtle()
avatar.shape(avatar_image)

monster_image = "Enemy.gif"
wn.addshape(monster_image)
monster = trtl.Turtle()
monster.shape(monster_image)
monster.penup()
monster.goto(rand.randrange(-280, 221, 20), rand.randrange(-220, 221, 20))
monster.pendown()

def gen_problem():
  for problems in range(3):
    num1, num2 = rand.randrange(1,31), rand.randrange(1,16)
    operator = ["+", "-", "*", "/"]
    operation = rand.choice(operator)
    if mode == "Easy":
      operation = "+"
      answer = num1 + num2
    elif mode == "Medium":
      operator = ["+", "-"]
      operation = rand.choice(operator)
      if operation == "-":
        while num1 < num2:
          num1 = rand.randrange(15,31)
        answer = num1 - num2
      elif operation == "+":
        answer = num1 + num2
    elif mode == "Hard":
      operator = ["*", "/"]
      operation = rand.choice(operator)
      if operation == "*":
        answer = num1 * num2
      elif operation == "/":
        while num1 % num2 != 0:
          num1 = rand.randrange(51, 201)
        answer = num1 / num2
    user_answer = wn.textinput("Solve this Math problem: ", f"{num1}{operation}{num2}")
    if problems == 2 and int(user_answer) == answer:
      wn.textinput("Congratulations", "You Beat the Monster!")
    elif int(user_answer) != answer:
      wn.textinput("Game Over", "The Monster Outsmarted You")
      break

def right():
  avatar.setheading(0)
  avatar.forward(40)
  avatar.clear()
  if (avatar.distance(monster)) < 81:
    gen_problem()
  
def left():
  avatar.setheading(180)
  avatar.forward(40)
  avatar.clear()
  if (avatar.distance(monster)) < 81:
    gen_problem()

def down():
  avatar.setheading(270)
  avatar.forward(40)
  avatar.clear()
  if (avatar.distance(monster)) < 81:
    gen_problem()

def up():
  avatar.setheading(90)
  avatar.forward(40)
  avatar.clear()
  if (avatar.distance(monster)) < 81:
    gen_problem()
    

wn.listen()
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")
wn.onkeypress(up, "Up")

wn.mainloop()

