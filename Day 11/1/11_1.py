#################################################################
###### https://adventofcode.com/2022/day/11 #####################
#################################################################

file = "test.txt"

DAY_NO = "11"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [line.strip('\n').strip() for line in rawInput]
splitInput = []
# temp = ''
# for row in cleanerInput:
# 	if row == ''

# print(cleanerInput)

class Monkey():

	def __init__(self) -> None:
		pass

	def addStartingItems(self, items):
		self.items = items
	
	def addEquation(self, equation):
		self.equation = equation
	
	def addTestCondition(self, testCondition):
		self.testCondition = testCondition
	
	def addTrueReult(self, testTrue):
		self.testTrue = testTrue
	
	def addFalseResults(self, testFalse):
		self.testFalse = testFalse


class Game():

	def __init__(self, input) -> None:
		self.unprocessedInput = input
		self.monkeyArr = []

	
	def processInput(self):
		monkeycount = 0
		for row in self.unprocessedInput:
			if row == '':
				monkeycount += 1
			
			elif row.split()[0] == 'Monkey':
				self.monkeyArr.append(Monkey())
			
			elif row.split()[0] == 'Starting':
				...
			# match 

		...
	

