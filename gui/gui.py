#!/usr/bin/env python2

from tkinter import *
import numpy as np
from game.engine import Engine
import game.constants

class GUI:

	def callback(self):
		print("fuck")

	def __init__(self, master):
		self.tiles = []
		self.master = master
		self.frame = Frame(master)

		Grid.rowconfigure(master, 0, weight=1)
		Grid.columnconfigure(master, 0, weight=1)
		self.frame.grid(row=0, column=0)



		e = Engine()
		e.setup_board()
		board = e.get_board(1)

		# board setup
		for i in range(10):
			Grid.rowconfigure(self.frame, i, weight=1)
			for j in range(10):
				Grid.columnconfigure(self.frame, j, weight=1)
				tile = Button(self.frame)
				tile.config(height=40,
							width=40,
							command=self.callback,
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