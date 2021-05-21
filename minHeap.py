class AdaptedHeap: # min_heap으로 정의함!
	def __init__(self):
		self.A = []
		self.D = {}  # dictionary D[key] = index

	def __str__(self):
		return str(self.A)
	def __len__(self):
		return len(self.A)

	def insert(self, key):
		# code here
		# key 값이 최종 저장된 index를 리턴한다!
		self.A.append(key)
		self.D[key]=len(self.A)-1
		self.heapify_up(len(self.A)-1)
		return self.D[key]

		def heapify_up(self, k):
		# code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
		p=(k-1)//2
		if p>=0 and self.A[p]>self.A[k]:
			self.D[self.A[k]],self.D[self.A[p]]=p,k
			self.A[k],self.A[p]=self.A[p],self.A[k]
			self.heapify_up(p)
			
	
	def heapify_down(self, k):
		# code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
		while 2*k+1<len(self.A):
			L,R = 2*k+1,2*k+2
			if self.A[L]<self.A[k]:
				m=L
			else :
				m=k
			if R<len(self.A) and self.A[R]<self.A[m]:
				m=R
			#m= A[k],A[L],A[R]중 최소값의 인덱스
			if m!=k:
				self.D[self.A[k]],self.D[self.A[m]]=m,k
				self.A[k],self.A[m]=self.A[m],self.A[k]
				k=m
			else:
				break
	def find_min(self):
		# 빈 heap이면 None 리턴, 아니면 min 값 리턴
		# code here
		if len(self.A)==0:
			return None
		return self.A[0]
		
	def delete_min(self):
		# 빈 heap이면 None 리턴, 아니면 min 값 지운 후 리턴
		# code here
		if len(self.A)==0:
			return None
		key=self.A[0]
		self.D[self.A[0]],self.D[self.A[len(self.A)-1]]=len(self.A)-1,0
		self.A[0],self.A[len(self.A)-1]=self.A[len(self.A)-1],self.A[0]
		del self.D[self.A[len(self.A)-1]]
		self.A.pop()
		self.heapify_down(0)
		return key
	
	def update_key(self, old_key, new_key):
		# old_key가 힙에 없으면 None 리턴
		# 아니면, new_key 값이 최종 저장된 index 리턴
		# code here
		if old_key in self.D:
			self.A[self.D[old_key]]=new_key
			self.D[new_key]=self.D[old_key]
			del self.D[old_key]
			if old_key<new_key:
				self.heapify_down(self.D[new_key])
			if old_key>new_key:
				self.heapify_up(self.D[new_key])
			
			return self.D[new_key]
		else:
			return None


H = AdaptedHeap()
while True:
	cmd = input().split()
	if cmd[0] == 'insert':
		key = int(cmd[1])
		loc = H.insert(key)
		print(f"+ {int(cmd[1])} is inserted")
	elif cmd[0] == 'find_min':
		m_key = H.find_min()
		if m_key != None:
			print(f"* {m_key} is the minimum")
		else:
			print(f"* heap is empty")
	elif cmd[0] == 'delete_min':
		m_key = H.delete_min()
		if m_key != None:
			print(f"* {m_key} is the minimum, then deleted")
		else:
			print(f"* heap is empty")
	elif cmd[0] == 'update':
		old_key, new_key = int(cmd[1]), int(cmd[2])
		idx = H.update_key(old_key, new_key)
		if idx == None:
			print(f"* {old_key} is not in heap")
		else:  
			print(f"~ {old_key} is updated to {new_key}")
	elif cmd[0] == 'print':
		print(H)
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")