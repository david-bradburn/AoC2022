#################################################################
###### https://adventofcode.com/2022/day/4 ######################
#################################################################

file = "input.txt"

DAY_NO = "4"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

cleaner_input = []
for raw_pair in raw_input:
	splitBoundString = []
	split_pair = raw_pair.strip('\n').split(",")
	for location in split_pair:
		splitBoundString += [location.split('-')]

	cleaner_input += [splitBoundString]


# print(cleaner_input)
# for a in cleaner_input:
# 	print(a)

class Space():

	def __init__(self, input_clean) -> None:
		self.pairs_data = input_clean
		self.contained_totals = 0

		self.PAIRONE = 0
		self.PAIRTWO = 1
		self.lowerbound = 0
		self.upperbound = 1

		self.main()

	def checkIfFullyContain(self, pair_data):
		if int(pair_data[self.PAIRONE][self.lowerbound]) <= int(pair_data[self.PAIRTWO][self.lowerbound]) and int(pair_data[self.PAIRONE][self.upperbound]) >= int(pair_data[self.PAIRTWO][self.upperbound]):
			print("Pair 1 contains pair 2")
			print(pair_data)
			self.contained_totals += 1
		elif int(pair_data[self.PAIRONE][self.lowerbound]) >= int(pair_data[self.PAIRTWO][self.lowerbound]) and int(pair_data[self.PAIRONE][self.upperbound]) <= int(pair_data[self.PAIRTWO][self.upperbound]):
			print("Pair 2 contains pair 1")
			print(pair_data)
			self.contained_totals += 1
		else:
			print("Neither pair contains the other")
			print(pair_data)
			pass

	def main(self):

		for pair in self.pairs_data:
			self.checkIfFullyContain(pair)

		print(self.contained_totals)

p1 = Space(cleaner_input)



