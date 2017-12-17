move = 349

class LinkedList:
	def __init__(self, index=0, next=None):
		self.next = next
		self.index = index
		if next == None:
			self.next = self

l = LinkedList()
for i in range(2017):
	for __ in range(move): l = l.next
	l2 = LinkedList(index=i+1, next=l.next)
	l.next = l2
	l = l.next

print(l.next.index)

second_element = 0
location = 0
for i in range(50000000):
	location = (location + move) % (i + 1)
	location += 1
	if location == 1:
		second_element = i+1

print(second_element)



