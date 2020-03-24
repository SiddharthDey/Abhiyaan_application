#the code can solve with expressions with BODMAS rule but cannot solve for unary operators or special functions like triginometric functions,ln,power etc
def isOperand(ch):
    c = ord(ch)
    if ch=='0' or ch=='1' or ch=='2' or ch=='3' or ch=='4' or ch=='5' or ch=='6' or ch=='7' or ch=='8' or ch=='9':
        return True
    elif c >= 97 and c <= 122: 
        return True
    elif c >= 65 and c <= 90: 
        return True
    else:
        return False

def isOperator(ch):
    if ch=='+' or ch=='-' or ch=='*' or ch=='/':
        return True
    else:
        return False

def operatorWeight(ch):
    if (ch=='+' or ch=='-'):
        weight = 1
    if (ch=='*' or ch=='/'):
        weight = 2
    return weight

def higherPrecedence(a,b):
    if operatorWeight(a)>=operatorWeight(b):
        return True
    if operatorWeight(a)<operatorWeight(b):
        return False

def compute(ch,a,b):
    if ch=='+':
        return str(int(a)+int(b))
    if ch=='-':
        return str(int(a)-int(b))
    if ch=='*':
        return str(int(a)*int(b))
    if ch=='/':
        return str(int(a)/int(b))

#the string enter should be a mathematical expression and number of characters should be less than 30
string = input("Enter the string\n")
length = len(string)
arr = [None] * 30
i = 0
j = 0
res = ""
#the operators and operands are put into an array to avoid confusion between numbers with different number of digits during computation

while (True):
    if i > length:
        break
    if string[i] == " " or string[i] == ",":
        i = i + 1
        continue
    if isOperator(string[i]) == True or string[i] == "(" or string[i] == ")":
        arr [j] = string [i]
        j = j + 1
        i = i + 1
        continue
    if isOperand(string[i]) == True:
        res = res + string[i]
        if i == length-1:
            arr[j] = res
            break
        if isOperator(string[i+1]) == True or string[i+1] == "(" or string[i+1] == ")" or string[i+1] == " ":
            arr [j] = res
            res = ""
            i = i + 1
            j = j + 1
            continue
        i = i + 1
k= 0
while(True):
    if arr[k] == None:
        break
    k = k + 1

str1 = arr[0:k]
stack = []
res = []

#the enter mathematical expression(infix expression) is first converted into a postfix expression using stack data structure
#stack data structure is used as a list
for i in range(0,k):
    if isOperator(str1[i])==True:
        while(len(stack)!=0 and stack[len(stack)-1]!="(" and higherPrecedence(stack[len(stack)-1],str1[i])==True):
           res.append(stack.pop()) 
        stack.append(str1[i])
    elif str1[i]=="(":
        stack.append(str1[i])
    elif str1[i]==')':
        while(len(stack)!=0 and stack[len(stack)-1]!="("):
            res.append(stack.pop())
        stack.pop()
    else:
        res.append(str1[i])
while(len(stack)!=0):
    res.append(stack.pop())
str2 = ''
for t in range(0,len(res)):
    str2 = str2 + res[t] + " "
print("The postfix expression is:")
print(str2)

#the postfix operation is then solved
s= []
for i in range(0,len(res)):
    if isOperator(res[i])==True:
        y = s.pop()
        x = s.pop()
        s.append(compute(res[i],x,y))
    else:
        s.append(res[i])
print("The solution is",s[0])


