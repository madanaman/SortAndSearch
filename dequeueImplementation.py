from Dequeue import Dequeue
d = Dequeue()
print(d.isEmpty())
d.addRear('element1')
d.printList()
d.addRear('2')
d.printList()
d.addFront('f1')
d.printList()
d.addFront('f2')
d.printList()
print(d.size())
print(d.removeFront())
print(d.removeRear())
d.printList()