#################################################################
###### https://adventofcode.com/2022/day/15 #####################
#################################################################
import re
import string

regex = re.compile(r'')


file = "test.txt"

DAY_NO = "15"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [i.strip("\n") for i in rawInput]
# for i in cleanerInput:
# 	print(i)


class Scan():

	def __init__(self, data) -> None:
		self.data = data
		self.beaconPositions = []
		self.sensorPositions = []
		self.processData()
	

	def processData(self):
		for line in self.data:
			partialstrip = line.strip("Sensor at x=").split(",")
			xs = int(partialstrip[0])
			p2 = partialstrip[1].strip(" y=").split(":")
			ys = int(p2[0])

			xb = int(p2[-1].split("=")[-1])
			yb = int(partialstrip[-1].strip(" y="))

			self.sensorPositions.append((xs, ys))
			if [xb, yb] not in self.beaconPositions:
				self.beaconPositions.append((xb, yb))

		print(self.sensorPositions)#
		print(self.beaconPositions)

	
	# def 

scan = Scan(cleanerInput)
				
