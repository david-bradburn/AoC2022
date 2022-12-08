#################################################################
###### https://adventofcode.com/2022/day/8 ######################
#################################################################
import numpy as np

file = "input.txt"

DAY_NO = "8"
PART = "2"

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
		self.scoreAbove = 0
		self.scoreRight = 0
		self.scoreDown = 0
		self.scoreLeft = 0

		

	def calScore(self):
		self.scenicScore = self.scoreAbove * self.scoreRight * self.scoreDown * self.scoreLeft
		return self.scenicScore
	
		
class Forest():

	def __init__(self, input) -> None:
		self.trees = input
		self.treesScore = np.zeros_like(self.trees, dtype=int)
		self.width, self.height = self.treesScore.shape
		print(self.width, self.height)
		self.visibleCount = 0
		# print(self.treesScore)

		self.populateForestVisability()

		print(np.amax(self.treesScore))
		# self.countVisible()
	
	def populateForestVisability(self):
		for row_index, row in enumerate(self.trees):
			for col_index, value in enumerate(row):
				tree = Tree()
				noTreesAbove = row_index
				for treesAbove in range(noTreesAbove):#up
					tree.scoreAbove += 1
					if value <= self.trees[row_index - treesAbove - 1][col_index]:
						break

				noTreesRight = (self.width - 1) - col_index
				for treesRight in range(noTreesRight):
					tree.scoreRight += 1
					if value <= self.trees[row_index][col_index+treesRight + 1]:
						break
				
				noTreesDown = (self.height - 1) - row_index
				for treesDown in range(noTreesDown):
					tree.scoreDown += 1
					if value <= self.trees[row_index + treesDown + 1][col_index]:
						break
				
				noTreesLeft = col_index
				for treesLeft in range(noTreesLeft):
					tree.scoreLeft += 1
					if value <= self.trees[row_index][col_index - treesLeft - 1]:
						break
				
				self.treesScore[row_index][col_index] = tree.calScore()
		
		print(self.treesScore)

	
	# def countVisible(self):
	# 	for row in self.treesVisable:
	# 		for value in row:
	# 			if value:
	# 				self.visibleCount += 1

	# 	print(self.visibleCount)




p1 = Forest(cleanerInput)