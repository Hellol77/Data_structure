import random
import time

def unique_n2(A):    
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i]==A[j]:
                print("NO")
                return                                 
    print("YES")

def unique_nlogn(A):    
    C=sorted(A)   
    for i in range(0,n-1):
        if C[i]==C[i+1]:
            print("NO")
            return           
    print("YES") 
            
def unique_n(A):
    B=[0 for i in range(2*n+1)]
    for i in range(0,len(A)):       
            if B[A[i]+n]==1:
                print("NO")
                return
            else :
                B[A[i]+n]=1          
    print("YES")


            
#input: 값의 개수 n
n=int(input())
# -n과 n사이의 서로 다른 값 n 개를 랜덤 선택해 A구성
A=random.sample(range(-n,n+1),n)

n2TimeStart=time.process_time()
unique_n2(A)
n2TimeEnd=time.process_time()

nlognTimeStart=time.process_time()
unique_nlogn(A)
nlognTimeEnd=time.process_time()

nTimeStart=time.process_time()
unique_n(A)
nTimeEnd=time.process_time()
print("unique_n2의 수행시간 : ",n2TimeEnd-n2TimeStart)
print("unique_nlogn의 수행시간 : ",nlognTimeEnd-nlognTimeStart)
print("unique_n의 수행시간 : ",nTimeEnd-nTimeStart)

#위의 세개의 함수를 차례대로 불러 결과 값 출력해본다
#당연히 모두 다르게 sample했으므로 yes가 세번 연속 출력되어야 한다
#동시에 각 함수의 실행시간을 측정해본다
#이러한 과정을 n을 100부터 10만까지 다양하게 변화시키면서 측정한다