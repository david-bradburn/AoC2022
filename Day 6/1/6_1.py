#################################################################
###### https://adventofcode.com/2022/day/6 ######################
#################################################################

file = "input.txt"

DAY_NO = "6"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()[0]

cleanedInput = rawInput.strip('\n')

class Radio():

	def __init__(self, input) -> None:
		self.packets = input
		self.buffer = ''

		self.main()

	
	def main(self):
		for packet_index, packet in enumerate(self.packets):
			if len(self.buffer) < 4:
				self.buffer += packet
			else: 
				self.shiftWindowOnBuffer(packet)
			
			if len(self.buffer) == 4:
				if not self.checkForRepeats():
					print(packet_index+1)
					print(self.buffer)
					break
					
			
			
			

		
		# for packet_index, packet in enumerate(self.packets):
		# 	if len(self.buffer) == 3:
		# 		if packet not in self.buffer:
		# 			print(packet_index)
		# 			self.buffer += packet
		# 			print(self.buffer)
		# 			break
				
		# 		else:
		# 			self.shiftWindowOnBuffer(packet)

		# 	else:
		# 		print(self.buffer)
		# 		assert len(self.buffer) < 3
		# 		self.buffer += packet

	def checkForRepeats(self):
		
		repeatsCount = 0
		for character_index, character in enumerate(self.buffer):
			temp = self.buffer
			temp = temp.replace(character, '', 1)
			# print(self.buffer)
			# print(temp)
			if character in temp:
				repeatsCount += 1
		
		if repeatsCount > 0:
			return True
		else:
			return False



	def shiftWindowOnBuffer(self, packet):
		self.buffer += packet
		self.buffer = self.buffer[1:]
		assert len(self.buffer) == 4


p1 = Radio(cleanedInput)
