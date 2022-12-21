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

	def setMonkeyNumber(self, no):
		self.monkeyNumber = no

	def addStartingItems(self, items: list):
		self.items = items
	
	def addEquation(self, equation: list):
		self.equation = equation
	
	def addTestCondition(self, testCondition):
		self.testCondition = testCondition
	
	def addTrueReult(self, testTrue):
		self.testTrue = testTrue
	
	def addFalseResults(self, testFalse):
		self.testFalse = testFalse

	def catchItem(self, thrownItem: int):
		self.items.append(thrownItem)

	def inspectItem(self, itemValue):
		newItemValue = 0
		


	def display(self):
		nameString = "----------Monkey {}----------\n".format(self.monkeyNumber)
		itemString = "Item(s): {}\n".format(self.items)
		operationString = "Operation: new = {} {} {}\n".format(*self.equation)
		testString = "Test: divisible by {}\n".format(self.testCondition)
		trueString = "  If true: throw to monkey {}\n".format(self.testTrue)
		falseString = "  If false: throw to monkey {}".format(self.testFalse)

		print(nameString + itemString + operationString + testString + trueString + falseString)


class Game():

	def __init__(self, input) -> None:
		self.unprocessedInput = input
		self.monkeyArr = []

		self.processInput()
		self.printAllMonkeys()
	
	def printAllMonkeys(self):
		for monkey in self.monkeyArr:
			monkey.display()

	
	def processInput(self):
		monkeycount = 1
		for row in self.unprocessedInput:
			if row == '':
				monkeycount += 1
			
			elif row.split()[0] == 'Monkey':
				print("--------Monkey {}-------".format(monkeycount - 1))
				self.monkeyArr.append(Monkey())
				self.monkeyArr[-1].setMonkeyNumber(monkeycount - 1)
			
			elif row.split()[0] == 'Starting':
				itemStr = row.replace(",", "").split()[2:]
				print(itemStr)
				temp = []
				for item in itemStr:
					temp.append(int(item))
				
				self.monkeyArr[-1].addStartingItems(temp)
			
			elif row.split()[0] == 'Operation:':
				temp = row.split()
				print(temp[-3:])
				self.monkeyArr[-1].addEquation(temp[-3:])

			elif row.split()[0] == 'Test:':
				temp = row.split()
				print(temp)
				self.monkeyArr[-1].addTestCondition(int(temp[-1]))

			elif row.split()[1] == 'true:':
				temp = row.split()
				print(temp[-1])
				self.monkeyArr[-1].addTrueReult(int(temp[-1]))
			
			elif row.split()[1] == 'false:':
				temp = row.split()
				print(temp[-1])
				self.monkeyArr[-1].addFalseResults(int(temp[-1]))
				


game = Game(cleanerInput)	

