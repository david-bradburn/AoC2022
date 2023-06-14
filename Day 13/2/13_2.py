#################################################################
###### https://adventofcode.com/2022/day/13 #####################
#################################################################

import ast

file = "input.txt"

DAY_NO = "13"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

stripedInput = [i.strip("\n") for i in rawInput if i != "\n"]
convertedInput = [ast.literal_eval(i) for i in stripedInput]
# print(convertedInput)


class distress_packets():

	def __init__(self, data) -> None:
		self.rawData = data

		self.rawData.append([[2]])
		self.rawData.append([[6]])

		self.inOrderCount = 0
		self.totalCount = 0

		self.orderedPackets = []


		print(self.rawData)
		self.main()
		self.displayOrderedPackets()

		self.find_2_and_6()


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

		# print("-----")
		# print(f"left_val: {left_val} \nright_val:{right_val}")

		left_val_is_list  = isinstance(left_val, list)
		left_val_is_int   = isinstance(left_val,  int)

		right_val_is_list = isinstance(right_val, list)
		right_val_is_int  = isinstance(right_val, int)

		left_is_none = (left_val == None)
		right_is_none = (right_val == None)

		if (left_val_is_int and right_val_is_int): ## both int
			# print("both int")
			if left_val < right_val:
				# print("left is lower than right, pair in right order")
				return 1
			elif left_val == right_val:
				# print("left_val is equal to right_val, continue")
				return 0
			else:
				# print("left val is greater than right val, pair in wrong order")
				return 2
					
			
		elif (left_val_is_list and right_val_is_list): ## both list
			# print("both list")
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
				# print("left list is out of elements while right is not")
				return 1
				
		elif (left_val_is_list and right_val_is_int):
			# print("list and int")

			#right_val is an int and left is  list (i hope)
			right_list = [right_val]
			left_val_iter = iter(left_val)
			right_val_iter = iter(right_list)
			if len(left_val) == 0:
				# print(f"left val {left_val} is empty in right order")
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
			# print("left and right are None, try in riht order?")
			return 1
		
		elif (left_is_none and not right_is_none):
			# print("left is empty and right is not, in right order")
			return 1
		
		elif (not left_is_none and right_is_none):
			# print("left is not empty and right is empty, in wrong order")
			return 2
		
		else:
			raise Exception("egg")	
					
		return orderVal

	def displayOrderedPackets(self):
		for packet in self.orderedPackets:
			print(packet)

	def find_2_and_6(self):
		two = [[2]]
		six = [[6]]

		two_index = self.orderedPackets.index(two) + 1
		six_index = self.orderedPackets.index(six) + 1

		print(two_index, six_index, two_index * six_index)
	
	def main(self):

		for index, unsortedPacket in enumerate(self.rawData):
			if len(self.orderedPackets) == 0:
				self.orderedPackets.append(unsortedPacket)

			else:
				insertIndex = 0
				for packet_index, sortedPacket in enumerate(self.orderedPackets):
					
					left = unsortedPacket
					right = sortedPacket

					insertIndex = packet_index

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
							break
						elif (orderVal == 2):
							break
						else:
							raise Exception("Inncorrect return value")
					
					# print(f"orderVal {orderVal}")
					
					if (orderVal == 0): # didn't run above loop i.e. left is empty
						# print(f"left is empty")
						orderVal = 1

					assert (orderVal == 1) or (orderVal == 2)

					if orderVal == 1:
						break

					
				
				if orderVal == 1:
					print("Packets are in right order, insert here")
					self.orderedPackets.insert(insertIndex, unsortedPacket)
				elif orderVal == 2:
					self.orderedPackets.append(unsortedPacket)

		

			
p1 = distress_packets(convertedInput)

# test = iter(list[1])
#wrong answers


