#################################################################
###### https://adventofcode.com/2022/day/9 ######################
#################################################################

file = "input.txt"

DAY_NO = "9"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = []

for instruction in rawInput:
	temp = instruction.strip('\n').split(' ')
	temp =  [temp[0], int(temp[1])]
	cleanerInput.append(temp)
# print(cleanerInput)

class Head():

	def __init__(self) -> None:
		self.x = 0
		self.y = 0
	
	def returnPosition(self):
		return (self.x, self.y)

class Tail():

	def __init__(self) -> None:
		self.x = 0
		self.y = 0
	
	def returnPositionTuple(self):
		return (self.x, self.y)

class Rope():

	def __init__(self, input) -> None:
		self.headInstructions = input
		
		self.tail = Tail()
		self.head = Head()
		self.tailPositionDict = {self.tail.returnPositionTuple(): 1}
		
		print(self.tailPositionDict)
		

		self.main()
	
	def moveHead(self, instruction):
		self.oldHeadPosition = (self.head.x, self.head.y)
		match instruction[0]:
			case 'R':
				self.head.x += 1
			
			case 'D':
				self.head.y += 1
			
			case 'L':
				self.head.x -= 1
			
			case 'U':
				self.head.y -= 1


	def checkDistanceOfHeadFromTail(self):
		dX = self.head.x - self.tail.x ## positive is right
		dY = self.head.y - self.tail.y ## positice is down

		return dX, dY
	
	def updateTailDict(self):
		tailPos = self.tail.returnPositionTuple()
		if tailPos not in self.tailPositionDict:
			self.tailPositionDict[tailPos] = 1
		else:
			self.tailPositionDict[tailPos] += 1

	def updateTailPosition(self):
		#move to where the head was unless too close
		dX, dY = self.checkDistanceOfHeadFromTail()
		if abs(dX) <= 1 and abs(dY) <= 1:
			pass

		else: ##move to old head position
			self.tail.x = self.oldHeadPosition[0]
			self.tail.y = self.oldHeadPosition[1]
			self.updateTailDict()

	def main(self):
		for instruction in self.headInstructions:
			direction = instruction[0]
			distance = instruction[1]
			for amount in range(distance):
				self.moveHead(direction)
				self.updateTailPosition()

		print(len(self.tailPositionDict))	

p1 = Rope(cleanerInput)