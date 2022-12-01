#################################################################
###### https://adventofcode.com/2022/day/1 ######################
#################################################################

file = "input.txt"

DAY_NO = "1"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

	raw_arr = []
	for item in raw_input:
		raw_arr += [item.strip('\n')]

# print(raw_arr)
total_cal_arr = []
temp = 0

for item in raw_arr:
	if item != '':
		temp += int(item)
	else:
		total_cal_arr += [temp]
		temp = 0

total_cal_arr += [temp]
total_cal_arr.sort()
print(total_cal_arr)

total_cal = 0
for i in range(3):
	total_cal += total_cal_arr[-1-i]

print(total_cal)