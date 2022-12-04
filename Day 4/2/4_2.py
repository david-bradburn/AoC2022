#################################################################
###### https://adventofcode.com/2022/day/4 ######################
#################################################################

file = "input.txt"

DAY_NO = "4"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

cleaner_input = []
for raw_pair in raw_input:
	splitBoundStringArr = []
	split_pair = raw_pair.strip('\n').split(",")
	for location in split_pair:
		splitBoundStringArr += [location.split('-')]

	splitBoundInt = []
	for pair in splitBoundStringArr:
		temp = []
		for bound in pair:
			temp += [int(bound)]
		splitBoundInt += [temp]

	cleaner_input += [splitBoundInt]


class Space():

	def __init__(self, input_clean) -> None:
		self.pairs_data = input_clean
		self.overlapTotal = 0

		self.PAIRONE = 0
		self.PAIRTWO = 1
		self.lowerbound = 0
		self.upperbound = 1

		self.main()

	def checkIfFullyContain(self, pair_data):
		# pair1LowerLessThanEqPair2Lower = pair_data[self.PAIRONE][self.lowerbound] <= pair[self.PAIRTWO][self.lowerbound]
		# pair1LowerGreaterThanEqPair2Upper = pair_data[self.PAIRONE][self.lowerbound] >= pair[self.PAIRTWO][self.upperbound]

		# pair1UpperLessThanEqPair2Lower = pair_data[self.PAIRONE][self.lowerbound] >= pair[self.PAIRTWO][self.upperbound]

	

		if pair_data[self.PAIRONE][self.lowerbound] <= pair_data[self.PAIRTWO][self.lowerbound] and pair_data[self.PAIRONE][self.upperbound] >= pair_data[self.PAIRTWO][self.upperbound]:
			print("Pair 1 contains pair 2")
			print(pair_data)
			self.overlapTotal += 1
		elif pair_data[self.PAIRONE][self.lowerbound] >= pair_data[self.PAIRTWO][self.lowerbound] and pair_data[self.PAIRONE][self.upperbound] <= pair_data[self.PAIRTWO][self.upperbound]:
			print("Pair 2 contains pair 1")
			print(pair_data)
			self.overlapTotal += 1
		
		elif pair_data[self.PAIRONE][self.lowerbound] <= pair_data[self.PAIRTWO][self.upperbound] and pair_data[self.PAIRTWO][self.lowerbound] <= pair_data[self.PAIRONE][self.lowerbound]:
			print('p2 upper greated')
			print(pair_data)

			self.overlapTotal += 1
		
		elif pair_data[self.PAIRONE][self.upperbound] >= pair_data[self.PAIRTWO][self.lowerbound] and pair_data[self.PAIRTWO][self.upperbound] >= pair_data[self.PAIRONE][self.upperbound]:
			self.overlapTotal += 1
		else:
			print("Neither pair overlaps")
			print(pair_data)
			

	def main(self):

		for pair in self.pairs_data:
			self.checkIfFullyContain(pair)

		print(self.overlapTotal)

p1 = Space(cleaner_input)



