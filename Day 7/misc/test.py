from anytree import NodeMixin, RenderTree, search


class Entry(NodeMixin):  # Add Node feature
    def __init__(self, name:str, itemType='None', size=0, parent=None, children=None):
        super(Entry, self).__init__()
        self.name = name
        self.size = size
        self.itemType = itemType

        self.parent = parent
        if children:  # set children only if given
            self.children = children
    
    def addChild(self, child: object):
        self.children = [*self.children, child]
    
    def display(self):
        for pre, fill, node in RenderTree(root):
            treestr = u"%s%s" % (pre, node.name)
            print(treestr.ljust(20), node.itemType, node.size)

    
def findfolder(self, path):
    temp = search.find(root, filter_ =lambda node: node.size == path)
    return temp



root = Entry('root', size=0, children=[
    Entry('my1', size=1),
    Entry('my2', size=2),])


for pre, fill, node in RenderTree(root):
    treestr = u"%s%s" % (pre, node.name)
    print(treestr.ljust(20), node.itemType, node.size)

root.addChild(Entry('my3', size=3))

temp = search.find(root, filter_ =lambda node: node.size == 3)
temp.addChild(Entry('my4', size=4))


temp = search.find(root, filter_ =lambda node: node.size == 3)
temp.addChild(Entry('my5', size=5))
# print(temp)

temp = search.find(root, filter_ =lambda node: node.size == 4)
temp.addChild(Entry('my6', size=6))
# print(temp)

root.display()


