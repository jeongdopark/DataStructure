# 스택의 응용 : 후위 표기 수식 계산

# 8 2 / 3 - 3 2 * +
def cal(arguments):
    stack = []
    for i in arguments:
        if i not in ('+', '-', '/', '*'):
            stack.append(int(i))
        else:
            if len(stack) < 2:
                return print('식을 다시 입력해주십시오')
            else:
                a = stack.pop()
                b = stack.pop()
                if(i == '+'):
                    stack.append(b+a)
                elif(i == '-'):
                    stack.append(b-a)
                elif(i == '*'):
                    stack.append(b*a)
                elif(i == '/'):
                    stack.append(b/a)
    return stack.pop()

test1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
print(cal(test1))                
