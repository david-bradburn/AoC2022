#################################################################
###### https://adventofcode.com/2022/day/11 #####################
#################################################################

import math


file = "input.txt"

DAY_NO = "11"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [line.strip('\n').strip() for line in rawInput]
splitInput = []

ofd = open("op.txt", "w")

class Monkey():

	def __init__(self) -> None:
		self.worryReductionValue = 3
		self.itemsInsepected = 0

	def setMonkeyNumber(self, no):
		self.monkeyNumber = no

	def addStartingItems(self, items: list):
		self.items = items
	
	def addEquation(self, equation: list):
		self.equation = equation
	
	def addTestCondition(self, testCondition : int):
		self.testCondition = testCondition
	
	def addTrueReult(self, testTrue):
		self.testTrue = testTrue
	
	def addFalseResults(self, testFalse):
		self.testFalse = testFalse

	def catchItem(self, thrownItem: int):
		self.items.append(thrownItem)

	def inspectItem(self, itemValue: int):
		# newItemValue = 0
		self.itemsInsepected += 1

		op1 = 0
		op2 = 0
		# operand = ""
		# print(self.equation)
		# print(itemValue)
		match self.equation[0]:
			
			case "old":
				op1 = itemValue
			
			case _:
				op1 = int(self.equation[0])
		
		match self.equation[2]:
			case "old":
				op2 = itemValue
			
			case _:
				op2 = int(self.equation[2])
		
		match self.equation[1]:
			case '+':
				# print(op1, "+" ,op2, op1 + op2)
				newValue = op1 + op2
			
			case '*':
				# print(op1, "*" ,op2, op1 * op2)
				newValue = op1 * op2
			
			case _:
				raise Exception("Need to add new operation type")


		return newValue % 223092870
		# if newValue > self.testCondition and newValue % self.testCondition != 0:
		# newValue %= self.testCondition
		# test = int(newValue % self.testCondition)
		# if test == 0:
		# 	return self.testCondition
		# # print(newValue, newValue % self.testCondition, test, test % self.testCondition)
		# tempMonkey = self.findMonkeyToThrowTo[]
		# assert((newValue % self.testCondition) == (test % self.testCondition))
	   
		# return test

	# def reduceItemWorry(self, itemValue):
	# 	newItemVal = math.floor(itemValue/self.worryReductionValue)
	# 	print(newItemVal)
	# 	return newItemVal

	def findMonkeyToThrowTo(self, itemValue):
		# print(itemValue%self.testCondition)
		if (itemValue % self.testCondition) == 0:
			# print(self.testTrue)
			return self.testTrue
		else:
			# print(self.testFalse)
			return self.testFalse
	
	



	def display(self):
		nameString = "----------Monkey {}----------\n".format(self.monkeyNumber)
		itemString = "Item(s): {}\n".format(self.items)
		operationString = "Operation: new = {} {} {}\n".format(*self.equation)
		testString = "Test: divisible by {}\n".format(self.testCondition)
		trueString = "  If true: throw to monkey {}\n".format(self.testTrue)
		falseString = "  If false: throw to monkey {}".format(self.testFalse)

		print(nameString + itemString + operationString + testString + trueString + falseString)
	
	def displayInspectedItemsCount(self):
		tempitem = "Monkey {} inspected items {} times".format(self.monkeyNumber, self.itemsInsepected)
		print(tempitem)
		# print("egg")



class Game():

	def __init__(self, input, fd) -> None:
		self.unprocessedInput = input
		self.monkeyArr = []

		self.fd = fd

		self.numRounds = 10000
		self.printEnable = False
		self.writeEnable = False

		self.processInput()
		# self.printAllMonkeys()

		self.main()
	
	def printAllMonkeys(self):
		for monkey in self.monkeyArr:
			monkey.display()

	def printAllItemCounts(self):
		for monkey in self.monkeyArr:
			monkey.displayInspectedItemsCount()

	def displayData(self, data):
		if self.printEnable:
			print(data)

	def writeData(self, data):
		if self.writeEnable:
			self.fd.write(str(data) + '\n')

	
	def processInput(self):
		monkeycount = 1
		for row in self.unprocessedInput:
			if row == '':
				monkeycount += 1
			
			elif row.split()[0] == 'Monkey':
				# print("--------Monkey {}-------".format(monkeycount - 1))
				self.monkeyArr.append(Monkey())
				self.monkeyArr[-1].setMonkeyNumber(monkeycount - 1)
			
			elif row.split()[0] == 'Starting':
				itemStr = row.replace(",", "").split()[2:]
				# print(itemStr)
				temp = []
				for item in itemStr:
					temp.append(int(item))
				
				self.monkeyArr[-1].addStartingItems(temp)
			
			elif row.split()[0] == 'Operation:':
				temp = row.split()
				# print(temp[-3:])
				self.monkeyArr[-1].addEquation(temp[-3:])

			elif row.split()[0] == 'Test:':
				temp = row.split()
				assert(int(temp[-1]) != 0)

				# print(temp)
				self.monkeyArr[-1].addTestCondition(int(temp[-1]))

			elif row.split()[1] == 'true:':
				temp = row.split()
				# print(temp[-1])
				self.monkeyArr[-1].addTrueReult(int(temp[-1]))
			
			elif row.split()[1] == 'false:':
				temp = row.split()
				# print(temp[-1])
				self.monkeyArr[-1].addFalseResults(int(temp[-1]))
	
	def main(self):
		self.printAllMonkeys()
		# self.writeData(1)
		print("--------------------------------------")
		for i in range(self.numRounds):
			if i % (self.numRounds/100) == 0:
				print("{}%".format(i * 100/self.numRounds))
			self.writeData("==========================")
			self.writeData("Round {}".format(i))
			self.writeData("==========================")
			for monkey in self.monkeyArr:
				self.writeData("--------Monkey {}--------".format(monkey.monkeyNumber))
				while monkey.items:
					item = monkey.items.pop(0)
					# self.writeData("Inspecting item {}".format(item))
					item = monkey.inspectItem(item)
					# self.writeData("New item value {}".format(item))
					# item = monkey.reduceItemWorry(item)
					nextMonkey = monkey.findMonkeyToThrowTo(item)
					# self.writeData("Next Monkey {}".format(nextMonkey))

					self.monkeyArr[nextMonkey].catchItem(item)
			
			# self.printAllMonkeys()
		
		self.printAllMonkeys()
		self.printAllItemCounts()


				


game = Game(cleanerInput, ofd)	

