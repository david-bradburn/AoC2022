#################################################################
###### https://adventofcode.com/2022/day/13 #####################
#################################################################

import ast

file = "input.txt"

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

		self.inOrderCount = 0
		self.totalCount = 0

		self.pair_data()

		# self.inOrderTemp = 0

		self.main()

		print(self.inOrderCount)
		print(self.totalCount)

	
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
		
	def eval_valOrder(self, valOrder):
		if(valOrder == 0):
			pass
		elif (valOrder == 2) or (valOrder == 1):
			return valOrder
		else:
			raise Exception("Inncorrect return value")
	
	# def pair_iter(self, left):
	# 	for left_item in left:

	def compare_pair(self, left_val, right_val):
		print("-----")
		print(f"left_val: {left_val} \nright_val:{right_val}")
		match (left_val, right_val):
			
					
			case (int(), int()): 
				print("both int")
				if left_val < right_val:
					print("left is lower than right, pair in right order")
					# self.inOrderCount += 1
					return 1
					# print("In right order")
					# in right order
				elif left_val == right_val:
					print("left_val is equal to right_val, continue")
					return 0
					#in wrong order
				else:
					print("left val is greater than right val, pair in wrong order")
					return 2
					
			
			case (None, _) | (_, None):
				print(f"left is {left_val} and right is {right_val}")

				if(left_val == None) and (right_val == None):
					print(f"left and right val are None, continue")
					# print(f"left is {left_val} and right is {right_val}")
					## continue
					return 0

				elif left_val == None:
					print("left is None and right has not finished, pair in right order ")
					# print(f"left is {left_val} and right is {right_val}")
					## in right order
					# self.inOrderCount += 1
					return 1
					...
				elif (left_val != None) and (right_val == None):
					print("left has not finsihed and right has finished, pair in wrong order ")

					return 2
					# print("one is empty")

				else:
					raise Exception

			case (_, int()) | (int(),_):

				# print(f"{left_val} {right_val}")
				if type(right_val) == int:
					print("list and int")

					#right_val is an int and left is  list (i hope)
					right_list = [right_val]
					left_val_iter = iter(left_val)
					right_val_iter = iter(right_list)
					if len(left_val) == 0:
						# self.inOrderCount += 1
						return 1
					for n in left_val:
						orderVal = self.compare_pair(self.iterate_iter(left_val_iter), self.iterate_iter(right_val_iter))
					
						if(orderVal == 0):
							pass
						elif (orderVal == 2) or (orderVal == 1):
							return orderVal
						else:
							raise Exception("Inncorrect return value")
				
				elif type(left_val) == int:
					print("int and list")
					#left_val is an int
					left_list = [left_val]
					left_val_iter = iter(left_list)
					right_val_iter = iter(right_val)
					if len(left_list) == 0:
						# self.inOrderCount += 1
						return 1
					for n in left_list:
						orderVal = self.compare_pair(self.iterate_iter(left_val_iter), self.iterate_iter(right_val_iter))

						# print(orderVal)
						if(orderVal == 0):
							pass
						elif (orderVal == 2) or (orderVal == 1):
							return orderVal
						else:
							raise Exception("Inncorrect return value")

				else:
					print()
					raise Exception
				# print("list and int")

			case (_, _):
				# print(f"{left_val} {right_val}")
				# print()
				print("both list")
				# right_list = list[right_val]
				left_val_iter = iter(left_val)
				right_val_iter = iter(right_val)
				if len(left_val) == 0 and len(right_val) != 0:
					# self.inOrderCount += 1
					return 1
				elif len(left_val) == 0 and len(right_val) == 0:
					return 0

				for n in left_val:
					orderVal = self.compare_pair(self.iterate_iter(left_val_iter), self.iterate_iter(right_val_iter))

					# print(orderVal)
					if(orderVal == 0):
						pass
					elif (orderVal == 2) or (orderVal == 1):
						return orderVal
					else:
						raise Exception("Inncorrect return value")
					
		return 0

	
	def main(self):
		self.totalWrong = 0
		for pair_index, pair in enumerate(self.paired_data):
			print(f"-----------------------Pair {pair_index + 1}-----------------------")
			print(f"No of pairs in order {self.inOrderCount}")
			print(f"No of pairs out of order {self.totalWrong}")
			print(f"index count {self.totalCount}")
			# print(f"Pair {pair_index + 1}")
			left, right = pair

			print(f"left:{left} \nright:{right}")
			left_iter = iter(left)
			right_iter = iter(right)
			orderVal = 0

			
			# print(left)
			for i in left:
				left_val = self.iterate_iter(left_iter)
				right_val = self.iterate_iter(right_iter)

				# print(left_val, right_val)
				# print(left_iter_type, right_iter_type)
				orderVal = self.compare_pair(left_val, right_val)
				# print("egg", orderVal)
				if(orderVal == 0):
					pass
				elif (orderVal == 1):
					# self.
					self.inOrderCount += 1

					self.totalCount += (pair_index + 1)
					break
				elif (orderVal == 2):
					self.totalWrong += 1
					break
				else:
					raise Exception("Inncorrect return value")
			
			print(f"orderVal {orderVal}")
			
			if (orderVal == 0):
				# orderVal = 1
				self.inOrderCount +=1 
				self.totalCount += (pair_index + 1)
			
			# assert(self.totalWrong + self.inOrderCount) == (pair_index + 1)
		
		print(self.inOrderCount, self.totalWrong)
		assert (self.inOrderCount + self.totalWrong) == 150

		
p1 = distress_packets(convertedInput)

# test = iter(list[1])
