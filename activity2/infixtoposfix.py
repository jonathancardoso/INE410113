#!/usr/bin/python
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

operator = "+-*/^()"
priority = {}
priority['(']=0;
priority['+']=1;
priority['-']=1;
priority['*']=2;
priority['/']=2;
priority['^']=3;

def isOperator(character):
    if (operator.find(character) == -1):
        return False
    else:
        return True

def check(stack, string):
    aux = ""
    size = len(string)
    for j in range (0,size):
        element = string[j]
        if(not isOperator(element)):
            aux += element
        elif (element == '('):
            stack.push(element)
        elif (element == ')'):
            topElem = stack.pop()
            while (topElem != '('):
                aux += topElem
                topElem = stack.pop()
        else:
            while (not stack.isEmpty() and (priority[stack.peek()] >= priority[element])):
                aux += stack.pop()
            stack.push(element)
    while not stack.isEmpty():
        aux += stack.pop()
    return aux

n = int(raw_input()) #input number
for i in range (0,n):
    string = raw_input() #get the entry
    stack = Stack()
    postfix = check(stack, string)
    print(postfix)
