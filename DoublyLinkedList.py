class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # create an empty list with only dummy node
	
	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next
	def __str__(self):
		return " -> ".join(str(v.key) for v in self)

	def printList(self):
		v = self.head.next
		print("h -> ", end="") 
		while v != self.head:
			print(str(v.key)+" -> ", end="")
			v = v.next
		print("h")
		
	def splice(self,a,b,x):
		if a==None or b==None or x==None:
			return
		ap=a.prev
		bn=b.next
		#cut
		ap.next=bn
		bn.prev=ap
		#insert[a..b] after x
		xn=x.next
		xn.prev=b
		b.next=xn
		a.prev=x
		x.next=a
		
	def moveAfter(self,a,x):
		self.splice(a,a,x)
		
	def moveBefore(self,a,x):
		self.splice(a,a,x.prev)
		
	def insertBefore(self,x,key):
		self.moveBefore(Node(key),x)
		
	def insertAfter(self,x,key):
		self.moveAfter(Node(key),x)
		
	def pushFront(self,key):
		self.insertAfter(self.head,key)
		
	def pushBack(self,key):
		self.insertBefore(self.head,key)
		
	def deleteNode(self,x):
		if x==None or x==self.head:
			return
		x.prev.next,x.next.prev=x.next,x.prev
		
	def popFront(self):#None 이면 empty
		if self.isEmpty():
			return None
		key=self.head.next.key
		self.deleteNode(self.head.next)
		return key
		
	def popBack(self):#None 이면 empty
		if self.isEmpty():
			return None
		key=self.head.prev.key
		self.deleteNode(self.head.prev)
		return key
		
	def search(self,key):#노드 리턴 None 리턴하면 찾는 값이 없다
		
		v=self.head.next
		while v!=self.head:
			if v.key==key:
				return v
			v=v.next
		return None	
		
	def isEmpty(self):
		if self.head.next==self.head:
			return True
		else:
			return False
			
	def first(self):
		if self.isEmpty():
			return None
		return self.head.next
		
	def last(self):
		if self.isEmpty():
			return None
		return self.head.prev
		
	def findMax(self): #제일 큰 key리턴 None 리턴하면 empty
		if self.isEmpty():
			return None
		temp=self.head.next
		v=temp.key
		while temp.next!=self.head:
			if v>temp.next.key:
				temp=temp.next			
			else:
				v=temp.next.key
				temp=temp.next
		return v 
		
	def deleteMax(self): #제일 큰 key 리턴 None 리턴하면 empty
		if self.isEmpty():
			return None
		v=self.findMax()
		self.deleteNode(self.search(self.findMax()))
		return v
		
	def sort(self):
		L_sorted=DoublyLinkedList()
		while self.findMax()!=None:
			L_sorted.pushFront(self.deleteMax())
		return L_sorted