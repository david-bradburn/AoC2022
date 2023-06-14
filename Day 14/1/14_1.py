#################################################################
###### https://adventofcode.com/2022/day/14 #######################
#################################################################

file = "test.txt"

DAY_NO = "14"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanedInput = [i.strip("\n").split(" -> ") for i in rawInput]

print(cleanedInput)

class Cave():
	def __init__(self, wallCoords) -> None:
		self.rawWallCoords = wallCoords
		self.minX = 1000
		self.minY = 1000
		self.createWalls()
		pass
	
	# def checkMinX(self,x):
	# 	if x < 


	def createWalls(self):
		for wall in self.rawWallCoords:
			noWallPoints = len(wall)
			for point in wall:
				x, y = point.split(",")
				x, y = int(x), int(y)
				self.minX = min(x, self.minX)
				self.minY = min(y, self.minY)
				print(x,y)

		print(f"min x: {self.minX} \nmin y: {self.minY}")

cave = Cave(cleanedInput)