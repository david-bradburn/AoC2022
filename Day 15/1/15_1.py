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
for i in cleanerInput:
	print(i)


class Scan():

	def __init__(self, data) -> None:
		self.data = data
		self.beaconPositions = []
		self.processData()
	

	def processData(self):
		print(string.ascii_letters)
		for line in self.data:
			partialstrip = line.replace(" ","").strip(string.ascii_letters)
			# match line:
			# 	case "Sensor at x={xs}, y={ys}: closest beacon is at x={xb}, y={yb}":
			# 		print("rg")
			# 		# print(xs, ys)

scan = Scan(cleanerInput)
				
