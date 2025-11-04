class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.start=None
    def printList (self):
        nodeVal=self.start
        while nodeVal is not None:
            print(nodeVal.getData())
            nodeVal=nodeVal.getNext()

    def addNode (self,value):
        nodeVal=self.start
        while nodeVal.getNext() is not None:
            nodeVal=nodeVal.getNext()
        #x=Node(value)
        nodeVal.setNext(Node(value))

    def deleteNode (self,value):
        nodeVal=self.start
        previous=self.start
        while nodeVal.getNext() is not None:
            if nodeVal.getData() == value:
                previous.setNext(nodeVal.getNext())
                return
            else:
                previous=nodeVal
                nodeVal=nodeVal.getNext()


list1=LinkedList()
n1=Node("January")
n2=Node("February")
n3=Node("March")
n4=Node("April")
list1.start=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=Node("May")


list1.addNode("June")
list1.printList()
list1.deleteNode("May")
list1.printList()
