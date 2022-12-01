#################################################################
###### https://adventofcode.com/2022/day/1 ######################
#################################################################

file = "input.txt"

DAY_NO = "1"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

	raw_arr = []
	for item in raw_input:
		raw_arr += [item.strip('\n')]

print(raw_arr)
max_cal = 0
temp = 0
for item in raw_arr:
	if item != '':
		temp += int(item)
	else:
		if temp > max_cal:
			max_cal = temp
		
		temp = 0
print(max_cal)