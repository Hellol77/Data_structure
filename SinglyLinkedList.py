class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None

	def __str__(self):
		return str(self.key)


class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def __len__(self):
		return self.size

	def printList(self):  
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")

	def pushFront(self, key):
		new_Node = Node(key)
		new_Node.next = self.head
		self.head = new_Node
		self.size += 1

	def pushBack(self, key):
		new_Node = Node(key)
		if self.size == 0:
			self.head=new_Node
		else:
			tail = self.head
			while tail.next !=None:
				tail=tail.next
			tail.next=new_Node
		self.size+=1
	def popFront(self):
		# head 노드의 값 리턴. empty list이면 None 리턴
		if self.size==0:
			return None
		else:
			x=self.head
			key = x.key
			self.head = x.next
			self.size = self.size -1
			del x
			return key
	def popBack(self):
		# tail 노드의 값 리턴. empty list이면 None 리턴
		if self.size ==0:
			return None
		else:
			prev,tail=None,self.head
			while tail.next!=None:
				prev=tail
				tail=tail.next
			if prev ==None:
				self.head=None
			else:
				prev.next=tail.next
			key = tail.key
			del tail
			self.size -=1
			return key
	def search(self, key):
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		v=self.head
		while v!=None:
			if v.key==key:
				return v
			v=v.next
		return v
	def remove(self, x):
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		
		if x==None or self.size ==0:
			return False
		elif x==self.head:
			self.popFront()
			return True
		else:
			prev,tail=None,self.head
			while tail!=x:
				prev=tail
				tail=tail.next
			prev.next=tail.next
			del x	
		self.size = self.size -1	
		return True	
	def reverse(self, key):
	
		i=None
		j=self.head
		while j!=None:
			if j.key==key:
				break
			i=j
			j=j.next
		if j==None:
			return
		prev=j
		tail=j.next
		j.next=None
		if tail==None:
			return
		while tail.next!=None:
			temp=tail.next
			tail.next=prev
			prev=tail
			tail=temp
		if i==None:
			self.head=tail
			tail.next
		else:
			i.next=tail
		tail.next=prev	
	def findMax(self):
		# self가 empty이면 None, 아니면 max key 리턴
		if self.size==0:
			return None
		prev=self.head
		v=prev.key
		tail=prev.next
		while tail!=None:
			if v<tail.key:
				v=tail.key
				tail=tail.next
			elif v>=tail.key:
				tail=tail.next
		return v
	def deleteMax(self):
		# self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
		if self.size==0:
			return None
		x=self.findMax()
		self.remove(self.search(self.findMax()))
		return x
	def insert(self, k, val):
		if self.size<k:
			self.pushBack(val)
		else:
			num=0
			prev=self.head
			tail=prev.next
			if k==1:
				new_Node=Node(val)
				new_Node.next=tail
				prev.next=new_Node
				self.size += 1
				return
			while num<k-1:
				num+=1
				prev=tail
				tail=tail.next
			new_Node=Node(val)
			new_Node.next=tail
			prev.next=new_Node
			self.size += 1
			return
	def size(self):
		return self.size

L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "reverse":
		L.reverse(int(cmd[1]))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == "insert":
		L.insert(int(cmd[1]), int(cmd[2]))
		print(cmd[2], "is inserted at", cmd[1]+"-th position.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")