#!/usr/bin/env python2

from tkinter import *
import numpy as np
import game.engine
import game.constants
from engine import Engine

class GUI:

	def callback(self):
		# temp
		print("fuck")

	def __init__(self, master):
		self.tiles = []
		self.master = master
		self.frame = Frame(master)

		Grid.rowconfigure(master, 0, weight=1)
		Grid.columnconfigure(master, 0, weight=1)
		self.frame.grid(row=0, column=0)


		e = Engine()
		#e.run()
		#count = 1
		#state1 = e.player1.get_starting_state()
		state2 = e.player2.get_starting_state()
		#if(e.board.add_player(state1,1)):
		#	board = e.board.get_player_view(1)
		added_player = e.board.add_player(state2, 2)
		print(added_player)
        if added_player:
           	board = e.board.get_player_view(2)
		# board setup
		for i in range(10):
			Grid.rowconfigure(self.frame, i, weight=1)
			for j in range(10):
				Grid.columnconfigure(self.frame, j, weight=1)
				tile = Button(self.frame)
				tile.config(height=40,
							width=40,
#<<<<<<< Updated upstream
							command=self.callback,
							text=board[i][j]) #change this line
				#count += 1 #change this line
#=======
#							bg="grey",
#							fg="black",
#							highlightcolor="green",
#							activebackground="blue",
#							text = "")
#				tile.bind("<Button>", self.callback)
#>>>>>>> Stashed changes
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