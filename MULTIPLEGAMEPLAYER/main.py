from tkinter import *
from tkinter import filedialog
import os


root = Tk()
root.geometry("1280x800")

photo = PhotoImage(file="mpg.png")
label = Label(root, image = photo)
label.pack()

play_game = PhotoImage(file='opengame.png')

img_label = Label(image=play_game)
#img_label.pack(pady=20)

def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    #opens the files
    os.system('"%s"' % my_program)

def open_TTT():
    open_TTT = 'c:/MULTIPLEGAMEPLAYER/games/TicTacToe.py'
    os.system('"%s"' % open_TTT)



    

my_button = Button(root, image=play_game, command=open_program, borderwidth=0,)
my_button.pack(pady=0,)


my_button2 = Button(root, text="Open TicTacToe", command=open_TTT)
my_button2.pack(pady=20)


my_label = Label(root, text = "")
my_label.pack(pady=20)










root.mainloop()