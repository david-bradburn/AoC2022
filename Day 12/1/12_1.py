#################################################################
###### https://adventofcode.com/2022/day/12 #####################
#################################################################

file = "test.txt"

DAY_NO = "12"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()