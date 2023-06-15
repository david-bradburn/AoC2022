#################################################################
###### https://adventofcode.com/2022/day/14 #####################
#################################################################

import numpy as np

file = "input.txt"

DAY_NO = "14"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanedInput = [i.strip("\n").split(" -> ") for i in rawInput]

# print(cleanedInput)

class Cave():

	def __init__(self, wallCoords) -> None:
		self.rawWallCoords = wallCoords
		self.minX = 1000
		self.minY = 1000

		self.maxX = 0
		self.maxY = 0
		self.createWalls()
		self.sandFinalLoc = []
		# self.displayCave()

		self.noSandStopped = 0
		self.continuousSand = False
		self.main()
		print(f"{self.noSandStopped}")
		pass


	def displayCave(self):
		for y in range(0, self.maxY + 1):
			temp = ""
			for x in range(self.minX, self.maxX + 1):
				if [x, y] in self.walls:
					temp += "#"
				elif [x, y] in self.sandFinalLoc:
					temp += "o"
				else:
					temp += "."
			print(temp)

	def main(self):

		while not self.continuousSand:
			self.updateSand(500, 0)
			# self.screen_clear()
			# self.displayCave()
		self.displayCave()

	
	
	def screen_clear(self):

		LINE_UP = '\033[1A'
		LINE_CLEAR = '\x1b[2K'

		for i in range(self.maxY + 2):
			print(LINE_UP, end=LINE_CLEAR)


	def updateSand(self, sandCoord_x, sandCoord_y):
		if sandCoord_y > self.maxY:
			self.continuousSand = True
			return

		if not([sandCoord_x, sandCoord_y + 1] in (self.walls + self.sandFinalLoc)):
			sandCoord_y += 1
			# self.dropSand(sandCoord_x, sandCoord_y)
		elif not ([sandCoord_x - 1, sandCoord_y + 1] in (self.walls + self.sandFinalLoc)):
			sandCoord_x -= 1
			sandCoord_y += 1
			
		elif not ([sandCoord_x + 1, sandCoord_y + 1] in (self.walls + self.sandFinalLoc)):
			sandCoord_x += 1
			sandCoord_y += 1
		else:
			# print("sand has come to rest")
			self.sandFinalLoc.append([sandCoord_x, sandCoord_y])
			self.noSandStopped += 1
			return

		self.updateSand(sandCoord_x, sandCoord_y)
		
			


	def createWalls(self):
		lessRawWallPoints = []
		for wall in self.rawWallCoords:
			noWallPoints = len(wall)
			temp = []
			for point in wall:
				x, y = point.split(",")
				x, y = int(x), int(y)
				self.minX = min(x, self.minX)
				self.minY = min(y, self.minY)

				self.maxX = max(x, self.maxX)
				self.maxY = max(y, self.maxY)
				# print(x,y)

				temp.append((x,y))
			lessRawWallPoints.append(temp)
		# print(lessRawWallPoints)
		# print(f"min x {self.minX} min y {self.minY}")
		# print(f"max x {self.maxX} max y {self.maxY}")

		self.walls = []
		for wall in lessRawWallPoints:
			# print("------------------------")
			for point_index in range(len(wall) - 1):
				x0 = wall[point_index][0]
				x1 = wall[point_index+ 1][0]

				y0 = wall[point_index][1]
				y1 = wall[point_index + 1][1]

				step = max(abs(x0 - x1), abs(y0 - y1))
				
				assert(step > 0)
				temp = np.linspace(wall[point_index], wall[point_index+1], step + 1, dtype=int).tolist()

				for point in temp:
					if point not in self.walls:
						self.walls.append(point)

			# print(self.walls)


cave = Cave(cleanedInput)