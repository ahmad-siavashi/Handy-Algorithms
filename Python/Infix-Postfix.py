# In his exalted name
# Algorithm: Infix to Posfix/Prefix
# Author: Ahmad Siavashi (ahmad.siavashi@gmail.com)
# Date: 11/9/2013

def EvaluateParentheses(Data):
    Stack = []
    for Data in Data :
        if Data == '(' :
            Stack.append(Data)
        elif Data == ')' :
            try :
                if Stack[-1] == '(' :
                    Stack.pop()
            except :
                return False
    if len(Stack) == 0 :
        return True
    else :
        return False

def InfixToPostfix(Data):
    Privilages = { '^' : 20, '*' : 10, '/' : 10, '+' : 5, '-' : 5, '=' : 2, '(' : 1 }
    Stack = []
    Postfix = []
    Infix = Data.split()
    for Data in Infix :
        if Data in '(=' :
            Stack.append(Data)
        elif Data == ')' :
            while Stack[-1] != '(' :
                Postfix.append(Stack.pop())
            Stack.pop()
        elif Data in '+-*/^' :
            while Stack != [] and Privilages[Stack[-1]] >= Privilages[Data] :
                Postfix.append(Stack.pop())
            Stack.append(Data)
        else :
            Postfix.append(Data)
    while Stack != []:
        Postfix.append(Stack.pop())
    postfix = ""
    for Element in Postfix :
        postfix += Element + " "
    return postfix

def InfixToPrefix(Data):
    Privilages = { '^' : 20, '*' : 10, '/' : 10, '+' : 5, '-' : 5, '=' : 2, ')' : 1 }
    Stack = []
    Prefix = []
    Infix = Data.split()
    Infix.reverse()
    for Data in Infix :
        if Data in ')' :
            Stack.append(Data)
        elif Data == '(' :
            while Stack[-1] != ')' :
                Prefix.insert(0,Stack.pop())
            Stack.pop()
        elif Data in '+-*/^' :
            while Stack != [] and Privilages[Stack[-1]] > Privilages[Data] :
                Prefix.insert(0,Stack.pop())
            Stack.append(Data)
        else :
            Prefix.insert(0,Data)
    while Stack != []:
        Prefix.insert(0,Stack.pop())
    PrefixExpression = ""
    for Element in Prefix :
        PrefixExpression += Element + " "
    return PrefixExpression

def Main():
    Data = raw_input("Please Enter Your Infix Expression : ")
    if EvaluateParentheses(Data) != True :
        print "The input string is not in a correct format."
        return False
    print InfixToPostfix(Data)
    print InfixToPrefix(Data)
    return True

Main()
