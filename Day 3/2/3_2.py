#################################################################
###### https://adventofcode.com/2022/day/3 ######################
#################################################################

file = "input.txt"

DAY_NO = "3"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

cleaner_input = []

for i in raw_input:
	cleaner_input += [i.strip('\n')]
# print(cleaner_input)

class Rucksacks():

	def __init__(self, items: list) -> None:
		self.allItems = items
		self.noOfRucksacks = len(self.allItems)
		self.priority_score = 0
		self.rucksackIndex = 0
		self.main()
		

	def findBadge(self, rucksack1, rucksack2, rucksack3):
		for item in rucksack1:
			if (item in rucksack2) and (item in rucksack3):
				print(item)
				self.priority_score += self.determinePriority(item)
				break


	def determinePriority(self, item):
		if item.islower():
			return ord(item) - 96
		else:
			return ord(item) - 38


	def getNextThreeRucksacks(self):
		rucksack1 = self.allItems[self.rucksackIndex]
		rucksack2 = self.allItems[self.rucksackIndex + 1]
		rucksack3 = self.allItems[self.rucksackIndex + 2]
		self.rucksackIndex += 3
		return rucksack1, rucksack2, rucksack3
	
	def main(self):
		while self.rucksackIndex < self.noOfRucksacks:
			rucksack1, rucksack2, rucksack3 = self.getNextThreeRucksacks()
			self.findBadge(rucksack1, rucksack2, rucksack3)
		print(self.priority_score)

rucksacks = Rucksacks(cleaner_input)
