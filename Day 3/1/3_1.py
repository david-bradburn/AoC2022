#################################################################
###### https://adventofcode.com/2022/day/3 ######################
#################################################################

file = "input.txt"

DAY_NO = "3"
PART = "1"

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
		self.priority_score = 0
		self.main()
		
	
	def splitInToRucksackHalves(self, items):
		lengthOfItems = len(items)
		
		assert lengthOfItems % 2 == 0
		halfWay = lengthOfItems // 2
		halfOne = items[:halfWay]
		halfTwo = items[halfWay:]
		
		return halfOne, halfTwo
	
	def compareCompartments(self, halfOne, halfTwo):
		for item in halfOne:
			if item in halfTwo:
				print(item)
				self.priority_score += self.determinePriority(item)
				break

	def determinePriority(self, item):
		if item.islower():
			return ord(item) - 96
		else:
			return ord(item) - 38



	
	def main(self):
		for rucksack in self.allItems:
			halfOne, halfTwo = self.splitInToRucksackHalves(rucksack)
			print(halfOne)
			print(halfTwo)
			self.compareCompartments(halfOne, halfTwo)
		print(self.priority_score)

rucksacks = Rucksacks(cleaner_input)
