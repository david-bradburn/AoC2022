#################################################################
###### https://adventofcode.com/2022/day/7 ######################
#################################################################

from anytree import NodeMixin, RenderTree, search, PreOrderIter

file = "input.txt"

DAY_NO = "7"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

cleanerInput = [i.strip('\n') for i in raw_input]
# print(cleanerInput)


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

		self.directorySize = 0
	
	def addFolder(self, folder):
		self.folderList.append(folder)

	def addFile(self, file):
		self.filesList.append(file)


class TheDiagram(NodeMixin):  # Add Node feature
	def __init__(self, name:str, itemType='', absolutePath = '', size=0, parent=None, children=None):
		super(TheDiagram, self).__init__()
		self.name = name
		self.size = size
		self.itemType = itemType
		self.absolutePath = absolutePath

		self.parent = parent
		if children:  # set children only if given
			self.children = children
    
	def addChild(self, child: object):
		self.children = [*self.children, child]
    
    


class Tree():

	def __init__(self, input) -> None:
		self.input = input
		# self.allFolders = []

		self.currentDirectory = ''
		self.directoryHistory = ['/']
		self.treeNetworkDict = {}
		self.minSizeToDelete = 30000000
		self.maxSize = 70000000
		self.total = 0
		self.root = TheDiagram('/', itemType='dir', absolutePath='/')
		# self.displayTree()
		self.main()
		# self.main()
	
	def main(self):
		for instr in self.input:
			self.createFileTree(instr)
		# self.displayTree()
		self.findDirectorySize(self.root)
		self.displayTree()
		self.findSmallestToDelete()
		# print(self.total)

	def returnFullParentPath(self):
		temp = ''
		for dir in self.directoryHistory:
			temp += dir + '_' 
		
		temp += self.currentDirectory
		return temp
	
	def returnFullPath(self, newDir):
		temp = ''
		for dir in self.directoryHistory:
			temp += dir + '_' 
		
		temp += self.currentDirectory + '_'
		temp += newDir
		return temp
	
	def displayTree(self):
		for pre, fill, node in RenderTree(self.root):
			treestr = u"%s%s" % (pre, node.name)
			print(treestr.ljust(20), node.itemType, node.size)
	
	def findFolder(self, path):
		temp = search.find(self.root, filter_ =lambda node: node.absolutePath == path)
		# print(temp)
		return temp


	
	def createFileTree(self, terminalLine):
		# print(terminalLine)
		splitTerminalLine = terminalLine.split(' ')
		match splitTerminalLine[0]:

			case '$': #command
				match splitTerminalLine[1]:

					case 'cd': ##change directory
						match splitTerminalLine[2]:
							case '..': ##move up tree
								self.currentDirectory = self.directoryHistory[-1]
								self.directoryHistory = self.directoryHistory[:-1]

							case '/': #'# move to root
								self.currentDirectory = '/'
								self.directoryHistory = []

							case _:
								self.directoryHistory.append(self.currentDirectory)
								self.currentDirectory = splitTerminalLine[2]
								# print(self.directoryHistory)

					case 'ls':
						pass #we can just skip this
			
			case 'dir':
				parentPath = self.returnFullParentPath()
				parentNode = self.findFolder(parentPath)
				childPath = self.returnFullPath(splitTerminalLine[1])
				parentNode.addChild(TheDiagram(splitTerminalLine[1], itemType='dir', absolutePath=childPath))
				pass

				
			case _:
				parentPath = self.returnFullParentPath()
				parentNode = self.findFolder(parentPath)
				childPath = self.returnFullPath(splitTerminalLine[1])
				parentNode.addChild(TheDiagram(splitTerminalLine[1], itemType='file', absolutePath=childPath, size=int(splitTerminalLine[0])))

				# print('File')
	
	def findDirectorySize(self, folder):
		tempSize = 0
		for child in folder.children:
			match child.itemType:
				case 'dir':
					tempSize += self.findDirectorySize(child)
				
				case 'file':
					# print("file {}, size {}".format(ch))
					tempSize += child.size

				case _:
					raise Exception

		folder.size = tempSize
		return tempSize
	
	def findSmallestToDelete(self):
		dirSizeArr = []
		for node in PreOrderIter(self.root):
			if node.itemType == 'dir':
				dirSizeArr.append(node.size)
		# print(dirSizeArr)
		sizeToDelete = self.root.size
		unusedSpace = self.maxSize - self.root.size
		# print(unusedSpace)
		spaceNeeded = self.minSizeToDelete - unusedSpace
		# print(spaceNeeded)
		for size in dirSizeArr:
			if (size < sizeToDelete) and size > spaceNeeded:
				sizeToDelete = size
		print(sizeToDelete)

	# def totalUpDirectories(self):
	# 	for node in PreOrderIter(self.root):
	# 		if node.itemType == 'dir' and (node.size <= self.MAXNODESIZE):
	# 			self.total += node.size


p1 = Tree(cleanerInput)
