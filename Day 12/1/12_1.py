#################################################################
###### https://adventofcode.com/2022/day/12 #####################
#################################################################

import numpy as np
import math

file = "input.txt"

DAY_NO = "12"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()



class Map():

	def __init__(self, rawInput) -> None:
		self.rawInput = rawInput

		BIGNUMBER = 999999999
		

		
		self.processInput()
		self.coordQueue = [self.startPosition]

		self.distanceMap = np.ones_like(self.map, dtype=int)
		self.distanceMap *= BIGNUMBER
		self.distanceMap[self.startPosition[1]][self.startPosition[0]] = 0
		print(self.distanceMap)
		# self.display()

		self.findSmallestdistance()

	def processInput(self):
		tempInput = []
		for row in self.rawInput:
			tempInput += [row.strip()]

		self.yMax = len(tempInput)
		self.xMax = len(tempInput[0])
		# print(self.height, self.width)
		self.map = np.zeros((self.yMax, self.xMax), dtype = int)
		for rowIndex, row in enumerate(tempInput):
			for coloumnIndex, value in enumerate(row):
				if value == 'S':
					self.map[rowIndex][coloumnIndex] = 0
					self.startPosition = (coloumnIndex, rowIndex)
				
				elif value == 'E':
					self.map[rowIndex][coloumnIndex] = 27
					self.endPosition = (coloumnIndex, rowIndex)
				
				else:
					self.map[rowIndex][coloumnIndex] = ord(value) - 96

		print(self.map)
		# print(tempInput)
	
	

	def findManhattanDistance(xstart, ystart, xcurent, ycurrent):
		return abs(xstart - xcurent) + abs(ystart - ycurrent)

	def returnCoordsRoundCurrentLocation(self, x, y):
		tempCoordArray = []
		if x - 1 >= 0:
			tempCoordArray.append((x - 1, y))
		if x + 1 < self.xMax:
			tempCoordArray.append((x + 1, y))
		
		if y - 1 >= 0:
			tempCoordArray.append((x, y - 1))
		
		if y + 1 < self.yMax:
			tempCoordArray.append((x, y + 1))

		return tempCoordArray
	
	def checkWeCanWalkThere(self, curpos: tuple, newcoords: list):
		currentHeight = self.map[curpos[1]][curpos[0]]
		tempLegalMoves = []
		for coord in newcoords:
			coordHeight = self.map[coord[1]][coord[0]]

			if currentHeight + 1 >= coordHeight:
				tempLegalMoves.append(coord)
		
		return tempLegalMoves



	def findSmallestdistance(self):
		while len(self.coordQueue) > 0:
			print("------------------------------------")
			currentCoord = self.coordQueue.pop(0)

			currentdistance = self.distanceMap[currentCoord[1]][currentCoord[0]]

			print(f"Current coord {currentCoord}")
			newCoords = self.returnCoordsRoundCurrentLocation(currentCoord[0], currentCoord[1])
			print(f"Potential coords {newCoords}")
			legalCoords = self.checkWeCanWalkThere(currentCoord, newCoords)

			for coord in legalCoords:
				newCoordDistance = self.distanceMap[coord[1]][coord[0]]

				newValue = currentdistance + 1
				if newValue < newCoordDistance:
					self.distanceMap[coord[1]][coord[0]] = newValue
					self.coordQueue.append(coord)
			
			print(f"Legal coords {legalCoords}")
			# print(self.distanceMap)

			# for coord in newCoords:
			# 	self.coordQueue.append(coord)

			# print(self.coordQueue)
		print(self.distanceMap)
		print(self.distanceMap[self.endPosition[1]][self.endPosition[0]])

		...


	

p1 = Map(rawInput)