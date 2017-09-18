class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next=self.head
        self.head = node

    def printl(self):
        current  = self.head
        while current:
            print current.data
            current= current.next

    def removeDups(self):
      current = second = self.head
      while current is not None:
          while second.next is not None:   # check second.next here rather than second
              if second.next.data == current.data:   # check second.next.data, not second.data
                  second.next = second.next.next   # cut second.next out of the list
              else:
                  second = second.next   # put this line in an else, to avoid skipping items
          current = second = current.next

    def kth(self, k):
      current = self.head
      for i in range(k):
        second = current.next
        current = current.next
      current = self.head
      while second:
        current = current.next
        second = second.next
        
      return current

    def delmid(self, n):
      current = self.head
      if current.data == n:
          print('Can\'t delete first node')
          return
      while current.next:
          if current.next.data == n:
              if current.next.next:
                  current.next = current.next.next
                  return
              else:
                  print('Can\'t delete last node')
                  return
          current = current.next

l= LinkedList()
l.insert(15)
l.insert(14)
l.insert(16)
l.insert(15)
l.insert(15)
l.insert(14)
l.insert(18)
l.insert(159)
l.insert(12)
l.insert(10)
l.insert(15)
l.insert(14)

l.printl()
print "==============="

l.removeDups()
l.printl()
print "+++++++++++++++"
print l.kth(3).data
l.delmid(159)
