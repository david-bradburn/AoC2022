#################################################################
###### https://adventofcode.com/2022/day/13 #####################
#################################################################

import ast

file = "test.txt"

DAY_NO = "13"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

stripedInput = [i.strip("\n") for i in rawInput if i != "\n"]
convertedInput = [ast.literal_eval(i) for i in stripedInput]
print(convertedInput)

class distress_packets():

	def __init__(self, data) -> None:
		self.rawData = data

	
	def pair_data(self):
		self.paired_data = []
		assert (len(self.rawData) % 2 == 0)
		for i in range(0, len(self.rawData), 2):
			self.paired_data[i] = [self.raw]