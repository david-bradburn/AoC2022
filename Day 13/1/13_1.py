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
	

	def compare_pair(self, left_val, right_val):



		print("-----")
		print(f"left_val: {left_val} \nright_val:{right_val}")

		left_val_is_list  = isinstance(left_val, list)
		left_val_is_int   = isinstance(left_val,  int)

		right_val_is_list = isinstance(right_val, list)
		right_val_is_int  = isinstance(right_val, int)

		left_is_none = (left_val == None)
		right_is_none = (right_val == None)

		if (left_val_is_int and right_val_is_int): ## both int
			print("both int")
			if left_val < right_val:
				print("left is lower than right, pair in right order")
				return 1
			elif left_val == right_val:
				print("left_val is equal to right_val, continue")
				return 0
			else:
				print("left val is greater than right val, pair in wrong order")
				return 2
					
			
		elif (left_val_is_list and right_val_is_list): ## both list
			print("both list")
			# right_list = list[right_val]
			left_val_iter = iter(left_val)
			right_val_iter = iter(right_val)
			if len(left_val) == 0 and len(right_val) != 0:
				
				return 1
			elif len(left_val) == 0 and len(right_val) == 0:
				return 1

			for n in left_val:
				orderVal = self.compare_pair(self.iterate_iter(left_val_iter), self.iterate_iter(right_val_iter))

				# print(orderVal)
				if(orderVal == 0):
					pass
				elif (orderVal == 2) or (orderVal == 1):
					return orderVal
				else:
					raise Exception("Inncorrect return value")
			
			if(orderVal == 0) and (len(left_val) < len(right_val)): ##
				return 1
		
		elif (left_val_is_int and right_val_is_list): ## left int right list
			print("int and list")
			#left_val is an int
			left_list = [left_val]
			left_val_iter = iter(left_list)
			right_val_iter = iter(right_val)
			if len(left_list) == 0:
				# self.inOrderCount += 1
				raise Exception("Int into list should not have length zero")
			for n in left_list:
				orderVal = self.compare_pair(self.iterate_iter(left_val_iter), self.iterate_iter(right_val_iter))

				# print(orderVal)
				if(orderVal == 0):
					pass
				elif (orderVal == 2) or (orderVal == 1):
					return orderVal
				else:
					raise Exception("Inncorrect return value")
				
			if(orderVal == 0) and (len(left_list) < len(right_val)): ##
				print("left list is out of elements while right is not")
				return 1
				
		elif (left_val_is_list and right_val_is_int):
			print("list and int")

			#right_val is an int and left is  list (i hope)
			right_list = [right_val]
			left_val_iter = iter(left_val)
			right_val_iter = iter(right_list)
			if len(left_val) == 0:
				print(f"left val {left_val} is empty in right order")
				return 1
			for n in left_val:
				orderVal = self.compare_pair(self.iterate_iter(left_val_iter), self.iterate_iter(right_val_iter))
			
				if(orderVal == 0):
					pass
				elif (orderVal == 2) or (orderVal == 1):
					return orderVal
				else:
					raise Exception("Inncorrect return value")
		
		elif(left_is_none and right_is_none): ## left is empty but right is not
			print("left and right are None, try in riht order?")
			return 1
		
		elif (left_is_none and not right_is_none):
			print("left is empty and right is not, in right order")
			return 1
		
		elif (not left_is_none and right_is_none):
			print("left is not empty and right is empty, in wrong order")
			return 2
		
		else:
			raise Exception("egg")	
					
		return orderVal

	
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


			for i in left:
				left_val = self.iterate_iter(left_iter)
				right_val = self.iterate_iter(right_iter)

				orderVal = self.compare_pair(left_val, right_val)
				# print("egg", orderVal)
				if(orderVal == 0):
					pass
				elif (orderVal == 1):
					# self.
					self.inOrderCount += 1
					print(f"Value added {pair_index + 1}")
					self.totalCount += (pair_index + 1)
					break
				elif (orderVal == 2):
					self.totalWrong += 1
					break
				else:
					raise Exception("Inncorrect return value")
			
			print(f"orderVal {orderVal}")
			
			if (orderVal == 0):
				print(f"pairs exactly match")
				
				self.inOrderCount +=1 
				print(f"Value added {pair_index + 1}")

				self.totalCount += (pair_index + 1)
				# raise Exception
			
			assert(self.totalWrong + self.inOrderCount) == (pair_index + 1)
		
		print(self.inOrderCount, self.totalWrong)
		assert (self.inOrderCount + self.totalWrong) == 150

		
p1 = distress_packets(convertedInput)

# test = iter(list[1])
#wrong answers
#4694

