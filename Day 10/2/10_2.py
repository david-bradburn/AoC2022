#################################################################
###### https://adventofcode.com/2022/day/10 #####################
#################################################################

import numpy as np

file = "test.txt"

DAY_NO = "10"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [line.strip('\n').split() for line in rawInput]
# print(cleanerInput)

class ComSystem():

	def __init__(self, input) -> None:
		self.input = input
		self.output = []
		self.regValue = 1
		self.clockCycleCounter = 0

		self.addxTime = 2

		

		self.cyclesToPrint = [19,59,99,139,179,219]
		self.display = []

		self.main()
	
	def updateRegister(self, value):
		self.regValue += value
	
	def incrementClockCount(self):
		self.clockCycleCounter += 1

	def addToOutput(self):
		self.output.append([self.clockCycleCounter, self.regValue])
	

	# def printOutput(self):
	# 	temp = 0
	# 	for line in self.output:
			
	# 		if line[0] in self.cyclesToPrint:
	# 			temp += (line[0]+ 1) * line[1]
	# 			print(line)
	# 	print(temp)

	def updateDisplay(self):
		pongPosition = [self.regValue - 1, self.regValue, self.regValue + 1]
		
		if self.clockCycleCounter in pongPosition:
			self.display.append('#')
		else:
			self.display.append('.')
	
	def displayScreen(self):
		output = np.reshape(self.display, (40, 6)).T
		# lengthDisplay = len(self.display)
		for row in output:
			temp = ''
			for value in row:
				temp += value
			print(temp)
		
	

	def main(self):
		for instruction in self.input:
			self.processInstruction(instruction)
		
		self.displayScreen()
		# self.printOutput()
		

	def processInstruction(self, instruction):
		opCode = instruction[0]
		if len(instruction) == 2:
			value = int(instruction[1])


		match opCode:
			case 'noop':
				##
				#here is during the cycle
				self.updateDisplay()
				##
				self.incrementClockCount()
				self.addToOutput()
			
			case 'addx':
				for instructionCycle in range(self.addxTime):
					##
					#here is during the cycle
					self.updateDisplay()
					##
					self.incrementClockCount()
					if instructionCycle == 1:
						self.updateRegister(value)
					self.addToOutput()
		


p1 = ComSystem(cleanerInput)