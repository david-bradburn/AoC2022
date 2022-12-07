#################################################################
###### https://adventofcode.com/2022/day/7 ######################
#################################################################

file = "test.txt"

DAY_NO = "7"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

cleanerInput = [i.strip('\n') for i in raw_input]
print(cleanerInput)


class File():
	def __init__(self, fileName: str, fileSize: int, parentDirectory: str) -> None:
		self.fileName = fileName
		self.fileSize = fileSize
		self.parentDirectory = parentDirectory

class Folder():
	def __init__(self, folderName: str, fileList: list, folderList: list, parentDirectory: str) -> None:
		self.folderName = folderName
		self.filesList = fileList
		self.folderList = folderList
		self.parentDirectory = parentDirectory
	
	def addFolder(self, folder):
		self.folderList.append(folder)

	def addFile(self, file):
		self.filesList.append(file)

class Tree():

	def __init__(self, input) -> None:
		self.tree = input
		self.allFolders = []

		self.currentDirectory = ''
		self.directoryHistory = []
		self.treeNetworkDict = {}
		self.main()
	
	def main(self):
		pass

	
	def createFileTree(self, terminalLine):
		splitTerminalLine = terminalLine.split(' ')
		match splitTerminalLine[0]:

			case '$': #command
				match splitTerminalLine[1]:

					case 'cd': ##change directory
						match splitTerminalLine[2]:
							case '..': ##move up tree
								self.currentDirectory = self.directoryHistory[-1]
								self.directoryHistory = self.directoryHistory[:-1]
								
							case _:
								self.currentDirectory = splitTerminalLine[2]
								self.directoryHistory.append(self.currentDirectory)

					case 'ls':
						pass #we can just skip this
			
			case 'dir':
				if splitTerminalLine[1] not in self.allFolders:
					self.allFolders.append(splitTerminalLine[1])
				
				tempDir = Folder(splitTerminalLine[1], [], [], self.currentDirectory)
				if self.currentDirectory not in self.treeNetworkDict:
					self.treeNetworkDict[self.currentDirectory] = [tempDir]
				


