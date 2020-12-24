# 스택의 응용 : 괄호 검사

def checkBrackets(argument):
    stack = []
    for ch in argument:
        if ch in ('{','[','('):
            stack.append(ch)
        elif ch in ('}', ']', ')'):
            if(len(stack) == 0):
                return False
            else:
                if(ch == '}' and stack.pop() != '{')or \
                (ch == ']' and stack.pop() != '[')or \
                (ch == ')' and stack.pop() != '('):
                    return False
    if(len(stack) == 0):
        return True
    else:
        return False


                    