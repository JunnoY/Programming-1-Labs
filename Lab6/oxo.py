from tkinter import Tk, PhotoImage, Button, messagebox #the module will allow us to create a window for GUI
window = Tk()
window.title("OXO Game")
window.geometry("300x300")
available_space = PhotoImage(file="myButton.png")
player1_taken = PhotoImage(file="myButtonP1.png")
player2_taken = PhotoImage(file="myButtonP2.png")
winner = PhotoImage(file="winner.png")

# create a list of squares, assign each element the value None
# [None, None, None, None, None, None, None, None, None]
square = [None]*9
def create_buttons():
    square[0] = Button(window, image=available_space, width="100", height="100", command = lambda:handle_button_click(0))
    square[0].place(x=0,y=0)
    square[1] = Button(window, image=available_space, width="100", height="100", command=lambda:handle_button_click(1))
    square[1].place(x=100, y=0)
    square[2] = Button(window, image=available_space, width="100", height="100", command=lambda:handle_button_click(2))
    square[2].place(x=200, y=0)
    square[3] = Button(window, image=available_space, width="100", height="100", command=lambda:handle_button_click(3))
    square[3].place(x=0, y=100)
    square[4] = Button(window, image=available_space, width="100", height="100", command=lambda:handle_button_click(4))
    square[4].place(x=100, y=100)
    square[5] = Button(window, image=available_space, width="100", height="100", command=lambda:handle_button_click(5))
    square[5].place(x=200, y=100)
    square[6] = Button(window, image=available_space, width="100", height="100", command=lambda:handle_button_click(6))
    square[6].place(x=0, y=200)
    square[7] = Button(window, image=available_space, width="100", height="100", command=lambda:handle_button_click(7))
    square[7].place(x=100, y=200)
    square[8] = Button(window, image=available_space, width="100", height="100", command=lambda:handle_button_click(8))
    square[8].place(x=200, y=200)
create_buttons()

counter = 0
def handle_button_click(button_number): #because we set button_click(number) in the 'command', which equals to the button_number here
    print("Button", button_number, "was clicked")
    global counter #put counter variable in global scope so that our function can access it
    if counter % 2 ==0:
        square[button_number].configure(image=player1_taken, command=square_taken) #!!!!IMPORTANT, Configure implies install image_player1_taken on square[number]
        update_move(button_number, 1)
    else:
        square[button_number].configure(image=player2_taken, command=square_taken) #if the first player has taken place, this time must be the 2nd player's
        update_move(button_number, 2)
    counter += 1

def square_taken():
    messagebox.showinfo("Square Taken", "Square already taken choose another!")

oxo=[
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def update_move(square_number, player_number):
    square_to_oxo_map = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2],
                         [2,0], [2,1], [2,2]] #It should be clear that square 1, maps to 0,1 of the oxo data structure
    m = square_to_oxo_map
    p = player_number
    s = square_number
    oxo[m[s][0]][m[s][1]] = p
    check_win()

def check_win():
    won = [] #store the results of if there is a win or not
    won.append(oxo[0][0]==oxo[1][1]==oxo[2][2] and oxo[0][0]!='')#斜线
    won.append(oxo[0][2]==oxo[1][1]==oxo[2][0] and oxo[0][2]!='') #斜线
    for row in range(3):
        won.append(oxo[row][0]==oxo[row][1]==oxo[row][2] and oxo[row][0]!='') # horizontal
    for col in range(3):
        won.append(oxo[0][col]==oxo[1][col]==oxo[2][col] and oxo[0][col]!='')# vertical

    #or we could have
        # for i in range(3):
        #     won.append(oxo[i][0] == oxo[i][1] == oxo[i][2] and oxo[i][0] != '
        #                , ')
        #     won.append(oxo[0][i] == oxo[1][i] == oxo[2][i] and oxo[0][i] != '
        #                ,')
    if True in won:
        button = Button(window, image=winner, width="300", height="100")
        button.pack()


window.mainloop() #display the window

