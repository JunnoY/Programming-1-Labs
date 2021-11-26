from tkinter import Tk, Canvas
import random

width = 550  # width of snake's world
height = 550  # height of snake's world


def setWindowDimensions(w, h):
    window = Tk()
    window.title("Snake Game")
    ws = window.winfo_screenwidth()  # computer screen size
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)  # calculate center point #why need to minus(w/2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # window size
    return window


window = setWindowDimensions(width, height)

# background
canvas = Canvas(window, bg='black', width=width,
                height=height)  # canvas allows us to draw objects such as rectangles and text boxes

# snake
snake = []  # create a list data structure to store our snake objects, the first object will be the snakes head, the remaining object will be the snakes body parts
snakeSize = 15
snake.append(canvas.create_rectangle(snakeSize, snakeSize, snakeSize * 2, snakeSize * 2, fill="white"))

# score
score = 0
txt = "Score:" + str(score)
# create a text object for the canvas for the score text
scoreText = canvas.create_text(width / 2, 10, fill="white", font="Times 20 italic bold", text=txt)


# define snake food
def placeFood():
    global food, foodX, foodY  # we global these three variables so we can use them in other functions later
    food = canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="steel blue")
    foodX = random.randint(0,
                           width - snakeSize)  # randomly generate some X and Y coordinates for the placement of the food
    foodY = random.randint(0, height - snakeSize)
    canvas.move(food, foodX, foodY)  # move the dood to the randomly generated coordinates


# define each key
def leftKey(event):
    global direction
    direction = "left"


def rightKey(event):
    global direction
    direction = "right"


def upKey(event):
    global direction
    direction = "up"


def downKey(event):
    global direction
    direction = "down"


# keyboard binding
canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.focus_set()
direction = "right"


# growing the snake
def growSnake():
    lastElement = len(
        snake) - 1  # subtract 1 becuase lists start with an index of 0. so the last element position is (the size of the list-1)
    lastElementPos = canvas.coords(
        snake[lastElement])  # get the coordinates of the last element (2 set of diagonal coordinates)
    snake.append(canvas.create_rectangle(0, 0, snakeSize, snakeSize,
                                         fill="#FDF3F3"))  # the size of the rectangle should be snakeSize*snakeSize
    # before we join the new square to the rest of the snake, we determine which direction the snake is moving
    if direction == "left":
        canvas.coords(snake[lastElement + 1], lastElementPos[0] + snakeSize, lastElementPos[1],
                      lastElementPos[2] + snakeSize, lastElementPos[3])
        # snake[lastElement+1] is the index of the new square
    elif direction == "right":
        canvas.coords(snake[lastElement + 1], lastElementPos[0] - snakeSize, lastElementPos[1],
                      lastElementPos[2] - snakeSize, lastElementPos[3])
    elif direction == "up":
        canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] + snakeSize, lastElementPos[2],
                      lastElementPos[3] + snakeSize)
    elif direction == "down":
        canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] - snakeSize, lastElementPos[2],
                      lastElementPos[3] - snakeSize)
    # increment of score
    global score
    score += 10
    txt = "score: " + str(score)
    canvas.itemconfigure(scoreText, text=txt)


# eating the food
def moveFood():
    global food, foodX, foodY
    canvas.move(food, (foodX * (-1)), (foodY * (
        -1)))  # move the food back to its original starting point (0,0) by multiplying the current coordinates by -1
    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)
    canvas.move(food, foodX, foodY)


# checking for collisions
def overlapping(a, b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[
        1]:  # a is one pair of positional coordinates and b is another pair
        return True
    return False


# moving the snake's head
def moveSnake():
    canvas.pack()  # pack any updates of our objects to the canvas 它将刚创建的控件通过打包的方法来放置到窗口中
    positions = []  # record the position of teh snake's head sothat his body can follow
    positions.append(canvas.coords(snake[0]))

    # check if the snakes head has left the canvas from:
    if positions[0][
        0] < 0:  # left #the first [0] is for the element in positions and the next [0] is for the element of the coordinate list
        canvas.coords(snake[0], width, positions[0][1], width - snakeSize, positions[0][3])
    elif positions[0][
        2] > width:  # for position[0][2], [0]=the first element which is the head and [2]means X-coordinate 2
        canvas.coords(snake[0], 0 - snakeSize, positions[0][1], 0, positions[0][3])
    elif positions[0][1] > height:
        canvas.coords(snake[0], positions[0][0], 0 - snakeSize, positions[0][2], 0)
    elif positions[0][3] < 0:
        canvas.coords(snake[0], positions[0][0], height, positions[0][2], height - snakeSize)
    positions.clear()  # clear the positions data in positions data structure
    positions.append(canvas.coords(snake[0]))  # append the postions of the snake's head to the data structure
    if direction == "left":
        canvas.move(snake[0], -snakeSize,
                    0)  # snake[0] is the head of the snake, and -snakeSize and 0 is the x and y coordinates respectively
    elif direction == "right":
        canvas.move(snake[0], snakeSize, 0)
    elif direction == "up":
        canvas.move(snake[0], 0, -snakeSize)
    elif direction == "down":
        canvas.move(snake[0], 0, snakeSize, )
        # using overlapping() and moveFood()
    sHeadPos = canvas.coords(snake[0])
    foodPos = canvas.coords(food)
    if overlapping(sHeadPos, foodPos):
        moveFood()
        growSnake()
    # make body links to head
    for i in range(1, len(snake)):
        positions.append(canvas.coords(snake[i]))
    for i in range(len(snake) - 1):
        canvas.coords(snake[i + 1], positions[i][0], positions[i][1], positions[i][2], positions[i][3])
    # head colliding with the body
    for i in range(1, len(snake)):
        if overlapping(sHeadPos, canvas.coords(snake[i])):
            gameOver = True
            canvas.create_text(width / 2, height / 2, fill="white", font="Times 20 italic bold", text="Game Over!")
    if 'gameOver' not in locals():
        window.after(90, moveSnake)  # increasing the first parameter#90 will decrease the game


placeFood()
moveSnake()
window.mainloop()  # this is a blocking method. this means any code after this instruction will not be executed until the window has been closed
