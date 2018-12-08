#!/usr/bin/env python2

from tkinter import *
import numpy as np
from game.engine import Engine
from game.player import Player
from utils.constants import *


class GUI:
    def ind_map_click(self, i, j):
        def map_click():
            #ignore if the current player ia an Ai
            if self.player1_turn and self.player1_config[Settings.AI.value]:
                return None
            if not self.player1_turn and self.player2_config[Settings.AI.value]:
                return None

            if self.button_counter % 2 is 0:
                self.clicked_buttons.append((i, j))
                self.button_counter += 1
            else:
                self.clicked_buttons.append((i,j))
                self.button_counter += 1
                p = self.e.player1
                if not self.player1_turn:
                  p = self.e.player2
                p.set_move(self.clicked_buttons)
                turn = self.e.make_move()
                #print(self.curselection())
                print(i, j)
                if turn == self.player1_turn:
                    self.clicked_buttons = []
                    self.button_counter = 0
                else:
                    self.clicked_buttons = []
                    self.button_counter = 0
                    self.player1_turn = not self.player1_turn
                    self.update()
                    if ((self.player1_turn and self.player1_config[Settings.AI.value]) or
                        (not self.player1_turn and self.player2_config[Settings.AI.value])):
                        print("manual move setting up next move")
                        self.master.after(MS_BETWEEN_MOVES, self.ai_move)
        return map_click


    def __init__(self, master):
        self.tiles = []
        self.textids = []
        self.master = master
        self.frame = Frame(master)
        self.canvas = Canvas(self.frame, width=510, height=510)

        Grid.rowconfigure(master, 0, weight=1)
        Grid.columnconfigure(master, 0, weight=1)
        self.frame.grid(row=0, column=0)

        self.player1_config = {
                Settings.AI.value : True, #should this be Ai or person
                Settings.START_TYPE.value : StartType.RANDOM.value, #what kind of start state
                Settings.START_PARAMS.value : [], #any parameters for the stater
                Settings.SEARCH_TYPE.value : SearchType.RANDOM.value, #what kind of search is happening
                Settings.SEARCH_PARAMS.value : [], #any parameters for the search
                Settings.AI_TYPE.value : AIType.NONE.value, # what is the AI
                Settings.AI_PARAMS.value : [] #any params for the ai
            }
        self.player2_config = {
                Settings.AI.value : True, #should this be Ai or person
                Settings.START_TYPE.value : StartType.RANDOM.value, #what kind of start state
                Settings.START_PARAMS.value : [], #any parameters for the stater
                Settings.SEARCH_TYPE.value : SearchType.RANDOM.value, #what kind of search is happening
                Settings.SEARCH_PARAMS.value : [], #any parameters for the search
                Settings.AI_TYPE.value : AIType.NONE.value, # what is the AI
                Settings.AI_PARAMS.value : [] #any params for the ai
            }

        self.tile_colors = [
        [
        "#DBE0FF", "#C7CCF7", "#B3B9EF", "#9FA6E8", "#8C92E0", "#787FD9",
        "#646CD1", "#5059CA", "#3D45C2", "#2932BB", "#151FB3", "#020CAC"
        ], [
        "#FFDBE0", "#F7C7CD", "#EFB3BB", "#E89FA8", "#E08C96", "#D97884",
        "#D16471", "#CA505F", "#C23D4D", "#BB293A", "#B31528", "#AC0216"]
        ]

        self.e = Engine(1000,self.player1_config, self.player2_config , False )
        self.e.setup_board()
        if not self.player1_config[Settings.AI.value]:
            board = self.e.get_board(1)
        else :
            board = self.e.get_board()
        self.win = False #winner trigger
        self.player1_turn = True #player 1 turn trigger
        self.winning_player = 0
        self.button_counter = 0
        self.clicked_buttons = []
        # board setup
        for i in range(10):
            for j in range(10):
                tag = i * 10 + j
                if board[i][j] == 111:
                    text_item = ""
                    tile_color = "white"
                    tile_outline = "white"
                elif board[i][j] == 0:
                    text_item = ""
                    tile_outline = "black"
                    tile_color = "grey"
                else:
                    text_item = str(board[i][j]%100)
                    tile_outline = "black"
                    tile_color = self.tile_colors[board[i][j]/100 - 2][board[i][j]%100 - 1]
                tile = self.canvas.create_rectangle(
                    j*50+10, i*50+10, j*50+50, i*50+50,
                    outline=tile_outline,
                    fill=tile_color,
                    activefill="cyan",
                    tags=tag)
                textid = self.canvas.create_text(
                    j*50+30, i*50+30, text=text_item, tags=str(tag)+"text")
                self.tiles.append(tile)
                self.textids.append(textid)
        self.canvas.grid(row=0, column=0)


    def ai_move(self):
        print("ai_move called")
        if self.player1_turn and not self.player1_config[Settings.AI.value]:
            return None
        if not self.player1_turn and not self.player2_config[Settings.AI.value]:
            return None

        self.player1_turn = self.e.make_move()
        self.update()

        winner = self.e.get_winner()
        if winner :
            #what do we want to happen on win
            pass
        else :
            if ((self.player1_turn and self.player1_config[Settings.AI.value]) or
                (not self.player1_turn and self.player2_config[Settings.AI.value])):
                print("ai move setting up next move")
                self.master.after(MS_BETWEEN_MOVES, self.ai_move)

    def update(self):
        #two ais playing
        if (self.player2_config[Settings.AI.value] and
            self.player1_config[Settings.AI.value]):

            board = self.e.get_board()

        #player 1 is manual and 2 is an ai
        elif (self.player2_config[Settings.AI.value] and
                not self.player1_config[Settings.AI.value]):

            board = self.e.get_board(1)

        #player 1 is an ai and 2 is manual
        elif (not self.player2_config[Settings.AI.value] and
                 self.player1_config[Settings.AI.value]):

            board = self.e.get_board(2)

        else: #both are manual players
            if self.player1_turn :
                board = self.e.get_board(1)
            else:
        	   board = self.e.get_board(2)

        for i in range(10):
            for j in range(10):
                if board[i][j] == 111:
                    text_item = ""
                    tile_color = "white"
                elif board[i][j] == 0:
                    text_item = ""
                    tile_color = "grey"
                else:
                    text_item = str(board[i][j]%100)
                    tile_color = self.tile_colors[board[i][j]/100 - 2][board[i][j]%100 - 1]
                self.canvas.itemconfig(self.tiles[i*10+j], fill=tile_color)
                self.canvas.itemconfig(self.textids[i*10+j], text=text_item)


def main():
    window = Tk()
    window.title("Stratego")
    window.geometry("510x510")
    window.resizable(0, 0)
    gui = GUI(window)

    if (gui.player1_config[Settings.AI.value]):
                print("main setting up next move")
                window.after(0, gui.ai_move)

    window.mainloop()


if __name__ == "__main__":
    main()