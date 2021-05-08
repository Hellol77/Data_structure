#
# HashOpenAddr 클래스 선언
# 
#commit
class HashOpenAddr:
    def __init__(self, size):
        self.size = size
        self.keys = [None]*self.size
        self.values = [0]*self.size
    
    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]
    def find_slot(self, key):
        i=self.hash_function(key)
        start=i
        while self.keys[i]!=None and self.keys[i]!=key:
            i=(i+1)%self.size
            if i == start :
                return None
        return i
    def set(self, key, value=1):
        i=self.find_slot(key)
        if i==None:
            return None
        if self.keys[i]!=None:
            self.values[i]=value
        else:
            self.keys[i]=key
            self.values[i]=value
        return key
    
    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
        i=self.find_slot(key)
        if self.keys[i]==None:
            return None
        j=i
        while True:
            self.keys[i]=None
            while True:
                j=(j+1)%self.size
                if self.keys[j]==None:
                    return key
                k=self.hash_function(self.keys[j])
                if not (i<k<=j or j<i<k or k<=j<i):
                    break
            self.keys[i]=self.keys[j]
            self.values[i]=self.values[j]
            i=j
                
    def search(self, key):
        i=self.find_slot(key)
        if self.keys[i]!=None:
            return self.keys[i]
        else:
            return None
    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)
# 입력

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
#
# 코드 (hash table을 이용해야 함)
#
Overlap_Result=[]
NonOverlap_Result=[]
if max(A)==1:
    Overlap=HashOpenAddr(2)
    NonOverlap=HashOpenAddr(2)
elif max(A)>=max(B):
    Overlap=HashOpenAddr(int(max(A)*1.5))
    NonOverlap=HashOpenAddr(int(max(A)*1.5))
elif max(A)<max(B):
    Overlap=HashOpenAddr(int(max(B)*1.5))
    NonOverlap=HashOpenAddr(int(max(B)*1.5))

#첫번째 줄 중복 모두 나열

for i in A:
    Overlap.set(i,Overlap.values[i]+1)
for i in B:
    Overlap.values[i]-=1
    if Overlap.values[i]<0:
        continue
    else:
        Overlap_Result.append(i)
for i in Overlap_Result:
    print(i,end=' ')
print('')
#두번째 줄 중복 제거 후 나열
for i in A:
    NonOverlap.set(i)
for i in B:
    if NonOverlap.remove(i)==None:
        continue
    else :
        NonOverlap_Result.append(i)
for i in NonOverlap_Result:
    print(i,end=' ')
        
