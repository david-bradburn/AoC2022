#################################################################
###### https://adventofcode.com/2022/day/5 ######################
#################################################################

import numpy as np

file = "input.txt"

DAY_NO = "5"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

rawBoard = []
rawMoves = []

blankLineFlag = False

for i in raw_input:
	rawLine = ''
	if not blankLineFlag:
		rawLine = i.strip('\n')
		if len(rawLine) == 0:
			blankLineFlag = True
		else:
			rawBoard += [i.strip('\n')]
	else:
		rawMoves += [i.strip('\n')]

class Ship():

	def __init__(self, rawBoard, rawMoves) -> None:
		self.cargo_size = 9
		self.cleanBoard(rawBoard[:-1])
		self.cleanMoves(rawMoves)
		print(self.Moves)

		self.processMoves()#
		print(self.Board)
		self.displayTopItems()
		pass

	def cleanBoard(self, rawBoard):
		# print(rawBoard)
		#4n +1
		self.Board = np.empty((self.cargo_size), dtype=list)
		for i in range(self.cargo_size):
			self.Board[i] = []

		# print(self.cleanBoard)
		for row in reversed(rawBoard):
			for stackNo in range(self.cargo_size):
				if row[4*stackNo + 1] != ' ':
					self.Board[stackNo].append(row[4*stackNo + 1])
				# print(row[4*stackNo + 1])

		# print(self.cleanBoard)
	
	def cleanMoves(self, rawMoves):
		self.Moves = []
		for move in rawMoves:
			# print(move.split())
			match move.split():
				case ["move", noMove, "from" , currentLoc, "to", newLoc]:
					self.Moves += [[int(noMove), int(currentLoc), int(newLoc)]]
				case _:
					raise Exception("oh no")

	def processMoves(self):
		for move in self.Moves:
			print(move)
			# itemBeingMoved = []
			
			itemBeingMoved = self.Board[move[1]-1][-move[0]:]
			self.Board[move[1]-1] = self.Board[move[1]-1][:-move[0]]
			print(itemBeingMoved)
			self.Board[move[2]-1] += itemBeingMoved
			print(self.Board)
	

	def displayTopItems(self):
		displayString = ''
		for i in range(self.cargo_size):
			if len(self.Board[i]) != 0:
				displayString += self.Board[i][-1]
		print(displayString)


ship = Ship(rawBoard, rawMoves)