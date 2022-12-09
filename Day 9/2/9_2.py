#################################################################
###### https://adventofcode.com/2022/day/9 ######################
#################################################################

file = "input.txt"

DAY_NO = "9"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = []

for instruction in rawInput:
	temp = instruction.strip('\n').split(' ')
	temp =  [temp[0], int(temp[1])]
	cleanerInput.append(temp)
# print(cleanerInput)

class RopeSegment():

	def __init__(self) -> None:
		self.x = 0
		self.y = 0
		self.oldX = 0
		self.oldY = 0

	def updateSegmentPosition(self, dx, dy):
		self.oldX = self.x
		self.oldY = self.y
		self.x += dx
		self.y += dy
		# prui
	
	def returnSegmentOldPosition(self):
		return (self.oldX, self.oldY)
	
	def returnOldNewPositionDelta(self):
		oldDx = self.x - self.oldX
		oldDy = self.y - self.oldY
		return  oldDx, oldDy


class Rope():

	def __init__(self, noSegments) -> None:
		self.ropeSegments = []

		for i in range(noSegments):
			self.ropeSegments.append(RopeSegment())

	def returnPositionNthSegmentTuple(self, segmentN: int):
		segment = self.ropeSegments[segmentN]
		return (segment.x, segment.y)
	
	def updateRopeSegmentPosition(self, ropeSegment, dx, dy):
		self.ropeSegments[ropeSegment].updateSegmentPosition(dx, dy)
	
	# def setTolocation(self, ropeSegment, x, y)


class Bridge():

	def __init__(self, input) -> None:
		self.headInstructions = input
		
		self.noSegments = 10
		self.rope = Rope(self.noSegments)
		
		self.tailPositionDict = {self.rope.returnPositionNthSegmentTuple(self.noSegments-1): 1}
		
		print(self.tailPositionDict)
		

		self.main()
	
	def moveHead(self, instruction):
		# self.oldHeadPosition = self.rope.returnPositionNthSegmentTuple(0) ##head position
		match instruction[0]:
			case 'R':
				self.rope.updateRopeSegmentPosition(0, 1, 0)
			
			case 'D':
				self.rope.updateRopeSegmentPosition(0, 0, -1)
		
			case 'L':
				self.rope.updateRopeSegmentPosition(0, -1, 0)
			
			case 'U':
				self.rope.updateRopeSegmentPosition(0, 0, 1)


	def checkDistanceOfAheadSegment(self, segmentNo):
		dX = self.rope.ropeSegments[segmentNo-1].x - self.rope.ropeSegments[segmentNo].x ## positive is right
		dY = self.rope.ropeSegments[segmentNo-1].y - self.rope.ropeSegments[segmentNo].y ## positive is up

		return dX, dY
	
	def updateTailDict(self):
		tailPos = self.rope.returnPositionNthSegmentTuple(self.noSegments - 1) 
		if tailPos not in self.tailPositionDict:
			self.tailPositionDict[tailPos] = 1
		else:
			self.tailPositionDict[tailPos] += 1

	def updateSegmentPosition(self, segmentNo):
		#move to where the head was unless too close
		dX, dY = self.checkDistanceOfAheadSegment(segmentNo)
		oldDx, oldDy = self.rope.ropeSegments[segmentNo - 1].returnOldNewPositionDelta()

		oldx, oldy = self.rope.ropeSegments[segmentNo-1].returnSegmentOldPosition()
		# curX, curY = self.rope.returnPositionNthSegmentTuple(segmentNo)
		# oldPositionDeltaX = oldx - curX
		# oldPositionDeltaY = oldy - curY


		if abs(dX) <= 1 and abs(dY) <= 1: ## still in range
			self.rope.updateRopeSegmentPosition(segmentNo, 0, 0)
		
		elif abs(oldDx) == 1 and abs(oldDy) == 1: ## check for diagonal motion
			if abs(dX) > 0 and abs(dY) > 0:
				self.rope.updateRopeSegmentPosition(segmentNo, oldDx, oldDy)
			else:
				self.rope.updateRopeSegmentPosition(segmentNo, int(dX/2), int(dY/2))

		# elif abs(oldDx) == 1 and abs(oldDy) == 1:
		# 	self.rope.updateRopeSegmentPosition(segmentNo, int(dX/2), int(dY/2))

		else: ##move to old segment position
			oldx, oldy = self.rope.ropeSegments[segmentNo-1].returnSegmentOldPosition()
			x, y = self.rope.returnPositionNthSegmentTuple(segmentNo)
			# print(oldx, oldy, x, y)
			
			self.rope.updateRopeSegmentPosition(segmentNo, oldx - x, oldy - y)
			# 

	def display(self):
		for i in range(self.noSegments):
			print("{} {}".format(i ,self.rope.returnPositionNthSegmentTuple(i)))

	def main(self):
		self.display()
		for instruction in self.headInstructions:
			direction = instruction[0]
			distance = instruction[1]
			
			print('---------{}:{}---------'.format(direction, distance))
			for amount in range(distance):
				
				self.moveHead(direction)
				# print(amount)
				# print('===========')
				
				for segmentNo in range(1, self.noSegments):
					# print(segmentNo)
					self.updateSegmentPosition(segmentNo)
				
				if direction == 'L' and distance == 8:
					print('--------')
					self.display()
				
				self.updateTailDict()
			self.display()
		print(len(self.tailPositionDict))

p1 = Bridge(cleanerInput)