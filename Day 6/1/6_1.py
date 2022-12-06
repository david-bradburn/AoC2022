#################################################################
###### https://adventofcode.com/2022/day/6 ######################
#################################################################

file = "test1.txt"

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

		self.checkForRepeats()

	
	def checkForRepeats(self):
		for packet_index, packet in enumerate(self.packets):
			if len(self.buffer) == 3:
				if packet not in self.buffer:
					print(packet_index)
					self.buffer += packet
					print(self.buffer)
					break
				
				else:
					self.shiftWindowOnBuffer(packet)

			else:
				print(self.buffer)
				assert len(self.buffer) < 3
				self.buffer += packet

	def shiftWindowOnBuffer(self, packet):
		self.buffer += packet
		self.buffer = self.buffer[1:]
		assert len(self.buffer) == 3


p1 = Radio(cleanedInput)
