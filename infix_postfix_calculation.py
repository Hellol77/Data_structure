class Stack:
    def __init__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

def get_token_list(expr):
    token_list=[]
    expr=expr.replace(' ','')# 공백 없애기
    listexpr=list(expr)
    while listexpr:
        if listexpr[0] in '+*-/^()':
            token_list.append(listexpr[0])
            del listexpr[0]
        else:
            if len(listexpr)==1:
                token_list.append(listexpr[0])
                del listexpr[0]
            else:
                for i in range(1,len(listexpr)):
                    
                           
                    if listexpr[i] in '+*-/^()':
                        token_list.append(''.join(listexpr[0:i]))
                        del listexpr[0:i]
                        break
                    elif i==len(listexpr)-1:
                        token_list.append(''.join(listexpr[0:len(listexpr)]))
                        del listexpr[0:len(listexpr)]
                        break
    return token_list
                        
def infix_to_postfix(token_list):
    outstack=[]
    opstack=Stack()
    #연산자 우선순위 설정
    prec={}
    prec['(']=0
    prec['+']=1
    prec['-']=1
    prec['*']=2
    prec['/']=2
    prec['^']=3
	
	
    for i in token_list:
        if i not in '+-*/^()':#연산자 피연산자 판별
            outstack.append(i)
        elif i =='(':
            opstack.push(i)
        elif i ==')':
            while True:
                outstack.append(opstack.pop())
                if opstack.top()=='(':
                    opstack.pop()
                    break
        else:
            if opstack.isEmpty():
                opstack.push(i)
            elif prec[i]>prec[opstack.top()]:
                opstack.push(i)
            elif prec[i]<=prec[opstack.top()]:
                while True:
                    if opstack.isEmpty():
                        opstack.push(i)
                        break
                    elif prec[i]>prec[opstack.top()]:
                        opstack.push(i)
                        break
                    elif prec[i]<=prec[opstack.top()]:
                        outstack.append(opstack.pop())
                        continue
    while not opstack.isEmpty():
        outstack.append(opstack.pop())	
    while True:
        try:
            outstack.remove('(')
            outstack.remove(')')
        except ValueError:
            break
    return outstack
def compute_postfix(token_list):
    resultstack=Stack()
    for i in token_list:
        if i not in '+-*/^':
            resultstack.push(float(i))
        elif i=='+':
            next_num=resultstack.pop()
            previous_num=resultstack.pop()
            resultstack.push(previous_num+next_num)
        elif i=='-':
            next_num=resultstack.pop()
            previous_num=resultstack.pop()
            resultstack.push(previous_num-next_num)
        elif i=='*':
            next_num=resultstack.pop()
            previous_num=resultstack.pop()
            resultstack.push(previous_num*next_num)
        elif i=='/':
            next_num=resultstack.pop()
            previous_num=resultstack.pop()
            resultstack.push(previous_num/next_num)
        elif i=='^':
            next_num=resultstack.pop()
            previous_num=resultstack.pop()
            resultstack.push(previous_num**next_num)
    return resultstack.pop()
			
			

expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)