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
# print(convertedInput)

class distress_packets():

	def __init__(self, data) -> None:
		self.rawData = data

		self.inOrder = 0

		self.pair_data()

		self.main()

	
	def pair_data(self):
		self.paired_data = []
		assert (len(self.rawData) % 2 == 0)
		for i in range(0, len(self.rawData), 2): # 
			self.paired_data.append([self.rawData[i], self.rawData[i+1]])

		# print(self.paired_data)

	def check_types(self, left, right):
		return type(left)
	
	# def pair_iter(self, left):
	# 	for left_item in left:
	
	def main(self):
		for pair in self.paired_data:
			left, right = pair

			print(left)
			for left_item in left:
				print(left_item, type(left_item))


p1 = distress_packets(convertedInput)
