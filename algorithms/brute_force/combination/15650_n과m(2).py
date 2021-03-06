# n과m(2)
# https://www.acmicpc.net/problem/15650
'''
# 선택 하거나 선택 안하거나
def solve(pos, cnt):
    if pos == n:
        if cnt == m:
            for i in range(n):
                if visit[i]:
                    print(i+1, end=' ')
            print()
        return
    visit[pos] = 1
    solve(pos+1, cnt+1)
    visit[pos] = 0
    solve(pos+1, cnt)
    return
n, m = map(int,input().split())
visit=[0]*n
solve(0, 0)
'''
#15649 처럼 푼 풀이
def solve(pos, cnt):
    if cnt == m:
        for i in range(m):
            print(stack[i]+1, end=' ')
        print()
        return
    for i in range(pos, n):
        if not visit[i]:
            visit[i] = 1
            stack.append(i)
            solve(i, cnt+1)
            stack.pop()
            visit[i] = 0
    return
n, m = map(int,input().split())
visit=[0]*n
stack = []
solve(0, 0)