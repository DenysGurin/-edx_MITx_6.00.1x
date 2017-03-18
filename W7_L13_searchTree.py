#binaryTree
class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None
    def setLeftBranch(self, node):
        self.leftBranch = node
    def setRightBranch(self, node):
        self.rightBranch = node
    def setParent(self, parent):
        self.parent = parent
    def getValue(self):
        return self.value
    def getLeftBranch(self):
        return self.leftBranch
    def getRightBranch(self):
        return self.rightBranch
    def getParent(self):
        return self.parent
    def __str__(self):
        return self.value
#DFTS
def DFSBinary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        print 'at node ' + str(queue[0].getValue())
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getRightBranch():
                queue.insert(0,temp.getRightBranch())
            if temp.getLeftBranch():
                queue.insert(0,temp.getLeftBranch())
    return False
#BFTS
def BFSBinary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        print 'at node ' + str(queue[0].getValue())
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
    return False
#create nodes
n5 = binaryTree(5)
n2 = binaryTree(2)
n8 = binaryTree(8)
n1 = binaryTree(1)
n4 = binaryTree(4)
n6 = binaryTree(6)
n3 = binaryTree(3)
n7 = binaryTree(7)
#create joins
n5.setLeftBranch(n2)
n5.setRightBranch(n8)
n2.setLeftBranch(n1)
n2.setRightBranch(n4)
n2.setParent(n5)
n8.setLeftBranch(n6)
n8.setParent(n5)
n1.setParent(n2)
n4.setLeftBranch(n3)
n4.setParent(n2)
n6.setRightBranch(n7)
n6.setParent(n8)
n3.setParent(n4)
n7.setParent(n6)

def fcn(node):
    return node.getValue() == 6
    
DFSBinary(n5, fcn)
BFSBinary(n5, fcn)