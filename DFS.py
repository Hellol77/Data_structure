import sys
sys.setrecursionlimit(5000)

def DFS(G, v):
	global curr_time # pre, post를 위한 time stamp
	# 그래프 G의 노드 v를 DFS 방문한다
	visited[v] = True
	print(v, end=' ')
	pre[v] = curr_time
	curr_time += 1
	for w in G[v]:
		if visited[w] is False:
			parent[w] = v
			DFS(G, w)
	post[v] = curr_time
	curr_time += 1

def DFSAll(G):
	# 그래프 G를 DFS 방문한다
	for v in range(n):
		if visited[v] == False:
			DFS(G, v)
	print()

# 입력 처리
n, m = [int(x) for x in input().split()]
G = [[] for _ in range(n)]
# G 입력 받아 처리
for _ in range(m):
	v, w = [int(x) for x in input().split()]
	G[v].append(w)
	G[w].append(v)
for v in range(n):
	G[v].sort()

# visited, pre, post 리스트 정의와 초기화
visited = [False for _ in range(n)]
pre = [-1 for _ in range(n)]
post = [-1 for _ in range(n)]
parent = [None for _ in range(n)]

# curr_time = 1로 초기화
curr_time = 1
DFSAll(G)

# 출력
for i, j in zip(pre, post):
	print(f"[{i}, {j}]", end=' ')