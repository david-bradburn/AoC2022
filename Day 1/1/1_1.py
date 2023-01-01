#################################################################
###### https://adventofcode.com/2022/day/1 ######################
#################################################################

file = "input.txt" ## name of the file that we want to load into python

DAY_NO = "1" ## Day number
PART = "1" ## Part number

# - works as a comment function and it not 'ran' or 'interpreted' by python 

file_path_base = "Day " + DAY_NO + "/misc/" ## the file path root to the file we want to load in
## looks like "Day 1/misc/"

with open(file_path_base + file, "r") as fd: ## this line opens the file from path "Day 1/misc/input.txt"
	## it calls the file reference "fd". so to do stuff to the file we use the "fd" variable to use and interact with it

	raw_input = fd.readlines() ##  this line actually does something to the file
	## it reads all the contents of the file and dumps into the variable raw_input, it should look like a list (array) of strings
	## e.g. [["asdas"], ["fjkhdsgfd"], ["...."], ...]

raw_arr = []
for item in raw_input:
	raw_arr += [item.strip('\n')]
##this section just process the input and cleans it up by removing the newline character "\n"


print(raw_arr)
max_cal = 0
temp = 0
for item in raw_arr: ## iterate through the list
	## for each item in the lsit raw_arr do the following code below
	if item != '': ## if the item is empty '' add the integer value of the string to a variable temp
		temp += int(item)
	else: ## else if the above condition is not true do the below code
		if temp > max_cal: ## check to see if the total is greater than the max total we've calculated previously
			max_cal = temp
		
		temp = 0 ## reset the temp value
print(max_cal) ## print the max val should by part 1 answer