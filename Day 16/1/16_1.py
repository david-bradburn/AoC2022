#################################################################
###### https://adventofcode.com/2022/day/16 #####################
#################################################################

file = "test.txt"

DAY_NO = "16"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()