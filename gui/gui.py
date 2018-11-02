#!/usr/bin/env python2

from tkinter import *
import numpy as np
from game.engine import Engine
from game.player import Player 
import utils.constants

class GUI:
    def ind_map_click(self, i, j):
        def map_click():
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
                turn = self.e.make_move(p)
                #print(self.curselection())
                print(i, j)
                if not turn:
                    self.clicked_buttons = []
                    self.button_counter = 0
                else:
                    self.clicked_buttons = []
                    self.button_counter = 0 
                    self.update()
        return map_click


    def __init__(self, master):
        self.tiles = []
        self.master = master
        self.frame = Frame(master)

        Grid.rowconfigure(master, 0, weight=1)
        Grid.columnconfigure(master, 0, weight=1)
        self.frame.grid(row=0, column=0)

        self.e = Engine()
        self.e.setup_board()
        board = self.e.get_board(1)
        self.win = False #winner trigger
        self.player1_turn = True #player 1 turn trigger
        self.winning_player = 0
        self.button_counter = 0
        self.clicked_buttons = []
        # board setup
        for i in range(10):
            Grid.rowconfigure(self.frame, i, weight=1)
            for j in range(10):
                Grid.columnconfigure(self.frame, j, weight=1)
                tile = Button(self.frame)
                tile.config(height=40,
                            width=40,
                            command = self.ind_map_click(i, j),
                            text=board[i][j])
                tile.grid(row=i, column=j)
                self.tiles.append(tile)
        

    def update(self):
        pass


def main():
    window = Tk()
    window.title("Stratego")
    window.geometry("500x500")
    window.resizable(0, 0)
    gui = GUI(window)

    window.mainloop()


if __name__ == "__main__":
    main()