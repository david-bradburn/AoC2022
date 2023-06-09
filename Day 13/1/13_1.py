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
		"""Converts N in to N/2 lots of 2"""
		self.paired_data = []
		assert (len(self.rawData) % 2 == 0)
		for i in range(0, len(self.rawData), 2): # 
			self.paired_data.append([self.rawData[i], self.rawData[i+1]])

		# print(self.paired_data)

	def iterate_iter(self, element_iter):
		try:
			return next(element_iter)
		except StopIteration:
			print("Empty list")
			return None
	
	# def pair_iter(self, left):
	# 	for left_item in left:
	
	def main(self):
		for pair in self.paired_data:
			print("------------------------------")
			left, right = pair

			left_iter = iter(left)
			right_iter = iter(right)

			
			# print(left)

			left_val = self.iterate_iter(left_iter)
			right_val = self.iterate_iter(right_iter)
			print(left_val, right_val)
			# print(left_iter_type, right_iter_type)

			match (left_val, right_val):
				
				case (int(), int()): 
					print("both int")
				
				case (None, _) | (_, None):
					print("one is empty")

				case (list, int()) | (int(), list):
					print("list and int")

				case (list, _) | (_, list):
					print("both list")

				case (_, _):
					raise Exception
					print("default")


			



p1 = distress_packets(convertedInput)