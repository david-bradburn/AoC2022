#################################################################
###### https://adventofcode.com/2022/day/12 #####################
#################################################################

import numpy as np

file = "test.txt"

DAY_NO = "12"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()



class Map():

	def __init__(self, rawInput) -> None:
		self.rawInput = rawInput
		
		self.processInput()
		# self.display()

	def processInput(self):
		tempInput = []
		for row in self.rawInput:
			tempInput += [row.strip()]

		self.height = len(tempInput)
		self.width = len(tempInput[0])
		# print(self.height, self.width)
		self.map = np.zeros((self.height, self.width), dtype = int)
		for rowIndex, row in enumerate(tempInput):
			for coloumnIndex, value in enumerate(row):
				if value == 'S':
					self.map[rowIndex][coloumnIndex] = 0
				
				elif value == 'E':
					self.map[rowIndex][coloumnIndex] = 27
				
				else:
					self.map[rowIndex][coloumnIndex] = ord(value) - 96

		print(self.map)
		# print(tempInput)
	

	

p1 = Map(rawInput)