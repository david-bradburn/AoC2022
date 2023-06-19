#################################################################
###### https://adventofcode.com/2022/day/15 #####################
#################################################################
import re
import string

regex = re.compile(r'')


file = "input.txt"

DAY_NO = "15"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [i.strip("\n") for i in rawInput]
for i in cleanerInput:
	print(i)


class Scan():

	def __init__(self, data) -> None:
		self.data = data
		self.beaconPositions = []
		self.sensorPositions = []

		self.sensorDict = {}

		self.maxDistance = 0
		self.processData()

		# self.minX = 0

		self.test_y = 10
		self.p1_y = 2000000

		self.count = 0

		self.checkNone()
		
	

	def processData(self):
		self.minX = 0
		self.maxX = 0
		for line in self.data:
			partialstrip = line.strip("Sensor at x=").split(",")

			xs = int(partialstrip[0])
			p2 = partialstrip[1].strip(" y=").split(":")
			ys = int(p2[0])

			xb = int(p2[-1].split("=")[-1])
			yb = int(partialstrip[-1].strip(" y="))

			self.minX = min(self.minX, xb)
			self.maxX = max(self.maxX, xb)
			self.sensorPositions.append((xs, ys))
			if (xb, yb) not in self.beaconPositions:
				self.beaconPositions.append((xb, yb))
			
			matDist = self.findMatDist((xs, ys), (xb, yb))
			self.sensorDict[(xs, ys)] = matDist
			self.maxDistance = max(self.maxDistance, matDist)

		print(self.sensorPositions)
		print(self.beaconPositions)
		print(self.minX, self.maxX)
		print(self.sensorDict)

	def findMatDist(self, sensorCoord, point):
		xs = sensorCoord[0]
		ys = sensorCoord[1]

		xp = point[0]
		yp = point[1]

		return abs(xs - xp) + abs(ys - yp)

	def findJumpDistance(self, checkCoord, sensorPos, sensorRadius):

		x, y = checkCoord


	def checkNone(self):
		self.noneCount = 0
		y = self.test_y
		# 4000000
		maxCoord = 4000000
		done  = 0
		x = 0
		y = 0
		while True:
			
			for sensorPosition in self.sensorPositions:
				if self.findMatDist((x, y), sensorPosition) <= self.sensorDict[sensorPosition]:
					x += (sensorPosition[0] - x) + self.sensorDict[sensorPosition] - abs(sensorPosition[1] - y) + 1
					# print(x,y)
					break
			else:
				print((x,y))
				break

			if x > maxCoord:
				y += 1
				x = 0
			
			if y > maxCoord:
				break		

		
		print(x*maxCoord + y)
		# print(self.count)

		# ...

	
	# def 

scan = Scan(cleanerInput)
				
