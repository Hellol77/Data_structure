class AdaptedHeap: # min_heap으로 정의함!
	def __init__(self):
		self.dist = []
	def __str__(self):
		return str(self.dist)
	def __len__(self):
		return len(self.dist)

	def insert(self,edgeWeight,edge):
		# code here
		# key 값이 최종 저장된 index를 리턴한다!
		self.dist.append([edgeWeight,edge])
		self.heapify_up(len(self.dist)-1)
		return

	def heapify_up(self, k):
		# code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
		p=(k-1)//2
		if p>=0 and self.dist[p][0]>self.dist[k][0]:
			self.dist[k],self.dist[p]=self.dist[p],self.dist[k]
			self.heapify_up(p)

	def heapify_down(self, k):
		# code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
		while 2*k+1<len(self.dist):
			L,R = 2*k+1,2*k+2
			if self.dist[L][0]<self.dist[k][0]:
				m=L
			else :
				m=k
			if R<len(self.dist) and self.dist[R][0]<self.dist[m][0]:
				m=R
			#m= A[k],A[L],A[R]중 최소값의 인덱스
			if m!=k:
				self.dist[k],self.dist[m]=self.dist[m],self.dist[k]
				k=m
			else:
				break

	def delete_min(self):
		# 빈 heap이면 None 리턴, 아니면 min 값 지운 후 리턴
		# code here
		key=self.dist[0]
		self.dist[0],self.dist[len(self.dist)-1]=self.dist[len(self.dist)-1],self.dist[0]
		self.dist.pop()
		self.heapify_down(0)
		return key[0],key[1]

nodeCount=int(input())
edgeCount=int(input())
totalDist=[100001]*nodeCount
graph=[[] for i in range(nodeCount)]
for i in range(edgeCount):
	u ,v, w=map(int, input().split())
	graph[u].append([v,w])
	
def dijkstra():
	distHeap=AdaptedHeap()
	distHeap.insert(0,0)
	totalDist[0]=0
	while len(distHeap)!=0:
		edgedist,edge = distHeap.delete_min()
		if totalDist[edge]<edgedist:
			continue
		for i in graph[edge]:
			newDist = edgedist+ i[1]
			if newDist<totalDist[i[0]]:
				totalDist[i[0]]=newDist
				distHeap.insert(newDist,i[0])
	
dijkstra()

for i in range(nodeCount):
	if totalDist[i]==100001:
		print('inf',end=' ')
	else:
		print(totalDist[i],end=' ')
	
	