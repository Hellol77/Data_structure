class myList():
	def __init__(self):
		self.capacity = 2	  # myList의 용량 (저장할 수 있는 원소 개수)
		self.n = 0          # 실제 저장된 값의 개수
		self.A = [None] * self.capacity # 실제 저장 자료구조 (python의 리스트 사용) 

	def __len__(self):
		return self.n
	
	def __str__(self):
		return f'  ({self.n}/{self.capacity}): ' + '[' + ', '.join([str(self.A[i]) for i in range(self.n)]) + ']'
	def __getitem__(self, k): # k번째 칸에 저장된 값 리턴
		if k>self.n-1 or k==0 or k<-(self.n):
			raise IndexError
		
		if k<0:	
			return self.A[self.n+k]
		else :
			return self.A[k]
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴

	def __setitem__(self, k, x): # k번째 칸에 값 x 저장
		if k>self.n-1 or k==0 or k<-(self.n):
			raise IndexError
		if k<0:
			self.A[self.n+k]=x
		else:	
			self.A[k]=x
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴

	def changing_size(self, new_capacity):
		print(f'  * changing capacity: {self.capacity} --> {new_capacity}') 
		B = [None] * new_capacity          
		for i in range(self.n):                
			B[i]=self.A[i]	     
		del self.A[0:]                      
		self.A=B                            
		self.capacity=new_capacity          
	
	def append(self, x):
		if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
			self.changing_size(self.capacity*2)
		self.A[self.n] = x          # 맨 뒤에 삽입
		self.n =self.n+1                 # n 값 1 증가

	def pop(self, k=None):               # A[k]를 제거 후 리턴. k 값이 없다면 가장 오른쪽 값 제거 후 리턴
		if self.n==0 or k>self.n-1 or k<-(self.n):  # 빈 리스트이거나 올바른 인덱스 범위를 벗어나면: 
			raise IndexError
			
		if self.capacity >= 4 and self.n <= self.capacity//4: # 실제 key 값이 전체의 25% 이하면 halving
			self.changing_size(self.capacity//2)
			
		
		if k<0:
			x=self.A[self.n+k]                
			for i in range(self.n+k,self.n-1): # pop(k)가 아닌 pop을 했을때 for문은 돌아가지 않는다
				self.A[i]=self.A[i+1]
			self.A[self.n-1]=None
			self.n-=1
			return x
		elif k>=0:
			x=self.A[k]                
			for i in range(k+1,self.n):
				self.A[i-1]=self.A[i]
			self.A[self.n-1]=None				     
			self.n-=1                  
			return x                   
		
		
	def insert(self, k, x):									# 주의: k 값이 음수값일 수도 있음
		if k>self.n-1:                 # k 값이 올바른 인덱스 범위를 벗어나면, raise IndexError
			raise IndexError                   
		if self.n == self.capacity:
			self.changing_size(self.capacity*2)
		for i in range(self.n,k,-1):          
			self.A[i]=self.A[i-1]
		self.A[k]=x                          
		self.n+=1                            
		
	def size(self):
		return self.capacity
		