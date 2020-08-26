from tkinter import *
from random import shuffle
from time import sleep

def reset():
    global window
    try:
        window.destroy()
    except NameError:
        pass
        #print("First Card")
        
    window = Tk()
    window.title("Digital Planet Bingo Card")

    topframe = Frame(window)
    topframe.pack()

    new = Button(topframe, text="Gererate New Card", command=reset)
    new.pack(side = LEFT)

    clear_button = Button(topframe, text="Clear Card", command=clear)
    clear_button.pack(side = LEFT)
    
    global words
    words = ["Facebook", "Twitter", "Google", "Algorithms", "Artificial\nIntelligence", "Machine\nLearning", "Online\nTrolls", "Data", "Africa", "Russia", "China", "India", "Ham\nRadio", "Climate\nChange", "Bias", "Internet\nShutdowns", "Virtual\nAssistants", "Cyber\nAttacks", "Smart\nMaterials", "Tracking", "Vulnerability", "Privacy"]
    shuffle(words)
    board = []
    for i in range(3):
        line = []
        for j in range(3):
            shuffle(words)
            line.append(words.pop())
        board.append(line)
            
    #print(board)
    card_generate(board)

def card_generate(board, word_width = 15, word_height = 5):
    global card
    global line1
    global line2
    global line3
    global word1
    global word2
    global word3
    global word4
    global word5
    global word6
    global word7
    global word8
    global word9
    
    card = Frame(window)
    word1 = Checkbutton(card, text=board[0][0], indicatoron=False, selectcolor="green", width=word_width, height=word_height)
    word2 = Checkbutton(card, text=board[0][1], indicatoron=False, selectcolor="green", width=word_width, height=word_height)
    word3 = Checkbutton(card, text=board[0][2], indicatoron=False, selectcolor="green", width=word_width, height=word_height)
    word4 = Checkbutton(card, text=board[1][0], indicatoron=False, selectcolor="green", width=word_width, height=word_height)
    word5 = Checkbutton(card, text=board[1][1], indicatoron=False, selectcolor="green", width=word_width, height=word_height)
    word6 = Checkbutton(card, text=board[1][2], indicatoron=False, selectcolor="green", width=word_width, height=word_height)
    word7 = Checkbutton(card, text=board[2][0], indicatoron=False, selectcolor="green", width=word_width, height=word_height)
    word8 = Checkbutton(card, text=board[2][1], indicatoron=False, selectcolor="green", width=word_width, height=word_height)
    word9 = Checkbutton(card, text=board[2][2], indicatoron=False, selectcolor="green", width=word_width, height=word_height)
    card.pack()
    word1.grid(column = 0, row = 0)
    word2.grid(column = 1, row = 0)
    word3.grid(column = 2, row = 0)
    word4.grid(column = 0, row = 1)
    word5.grid(column = 1, row = 1)
    word6.grid(column = 2, row = 1)
    word7.grid(column = 0, row = 2)
    word8.grid(column = 1, row = 2)
    word9.grid(column = 2, row = 2)

def clear():
    word1.deselect()
    word2.deselect()
    word3.deselect()
    word4.deselect()
    word5.deselect()
    word6.deselect()
    word7.deselect()
    word8.deselect()
    word9.deselect()

reset()

window.mainloop()
