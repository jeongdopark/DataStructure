


# 큐의 응용 : 너비우선탐색 BFS

from collections import deque

n = int(input())
graph = list(input().split() for _ in range(n))
 
def start():
    for i in range(n):
        for j in range(n):
            if(graph[i][j] == 'e'):
                return i, j
a, b = start()
def BFS(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = deque()
    stack.append((x, y))
    while stack:
        x, y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < n and 0 <= ny < n and (graph[nx][ny] == '0' or graph[nx][ny] == 'x')):
                if(graph[nx][ny] == 'x'):
                    return '성공'
                else:
                    graph[x][y] = '.'
                    stack.append((nx,ny))
    return '실패'
print(BFS(a, b))


        
