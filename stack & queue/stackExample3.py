# 스택의 응용 : 미로 탐색 DFS

n = int(input())
graph = list(input().split() for _ in range(n))
stack = []

a = 0
b = 0
# 시작  지점 찾는 함수
def start():
    global a, b
    for i in range(n):
        for j in range(n):
            if(graph[i][j] == 'e'):
                a = i
                b = j
                return a, b
start()
stack.append((a, b))
# 다음 지점 확인 하는 함수
def go(x, y):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    else:
        return graph[x][y] == '0' or graph[x][y] == 'x'

def DFS():
    while len(stack) != 0:
        print(stack)
        x, y = stack.pop()
        if(graph[x][y] == 'x'):
            return True
        else:
            graph[x][y] = '.'
            if go(x+1, y):
                stack.append((x+1, y))
            if go(x-1, y):
                stack.append((x-1, y))
            if go(x, y+1):
                stack.append((x, y+1))
            if go(x, y-1):
                stack.append((x, y-1))
    return False

if DFS():
    print('성공')
else:
    print('실패')

