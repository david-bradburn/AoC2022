#################################################################
###### https://adventofcode.com/2022/day/8 ######################
#################################################################
import numpy as np

file = "input.txt"

DAY_NO = "8"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

length = len(rawInput[0].strip('\n'))
height = len(rawInput)
print(length, height)
cleanerInput = np.zeros((length, height), dtype=int)

for row_index, row in enumerate(rawInput):
	for col_index, value in enumerate(row.strip('\n')):
		cleanerInput[row_index][col_index] = rawInput[row_index][col_index]

print(cleanerInput)

class Tree():

	def __init__(self) -> None:
		self.visibleFromUp = True
		self.visibleFromRight = True
		self.visibleFromDown = True
		self.visibleFromLeft = True

		self.treeVisible = None

	def checkIfVisiable(self):
		self.treeVisible = self.visibleFromUp or self.visibleFromRight or self.visibleFromDown or self.visibleFromLeft
		return self.treeVisible
	
# test = Tree()
# test.checkIfVisiable()
				
		
class Forest():

	def __init__(self, input) -> None:
		self.trees = input
		self.treesVisable = np.zeros_like(self.trees, dtype=bool)
		self.width, self.height = self.treesVisable.shape
		print(self.width, self.height)
		self.visibleCount = 0
		print(self.treesVisable)

		self.populateForestVisability()
		self.countVisible()
	
	def populateForestVisability(self):
		for row_index, row in enumerate(self.trees):
			for col_index, value in enumerate(row):
				tree = Tree()
				noTreesAbove = row_index
				for treesAbove in range(noTreesAbove):#up
					if value <= self.trees[row_index-treesAbove - 1][col_index]:
						tree.visibleFromUp = False
						break

				noTreesRight = (self.width - 1) - col_index
				for treesRight in range(noTreesRight):
					if value <= self.trees[row_index][col_index+treesRight + 1]:
						tree.visibleFromRight = False
						break
				
				noTreesDown = (self.height - 1) - row_index
				for treesDown in range(noTreesDown):
					if value <= self.trees[row_index + treesDown + 1][col_index]:
						tree.visibleFromDown = False
						break
				
				noTreesLeft = col_index
				for treesLeft in range(noTreesLeft):
					if value <= self.trees[row_index][col_index - treesLeft - 1]:
						tree.visibleFromLeft = False
						break
				
				self.treesVisable[row_index][col_index] = tree.checkIfVisiable()
		
		print(self.treesVisable)

	
	def countVisible(self):
		for row in self.treesVisable:
			for value in row:
				if value:
					self.visibleCount += 1

		print(self.visibleCount)




p1 = Forest(cleanerInput)