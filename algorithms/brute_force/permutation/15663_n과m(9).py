# https://www.acmicpc.net/problem/15663
# 굳이 사전 안써도 풀수있을듯??
from collections import*
def solve(cnt):
    if cnt == m:
        temp=[]
        for i in range(m):
            temp.append(q[i])
        temp = tuple(temp)
        if temp not in dic:
            dic[temp] = 1
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            q.append(arr[i])
            solve(cnt+1)
            q.pop()
            visit[i] = 0
n, m = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
dic = {}
q=deque()
visit=[0]*n
solve(0)
for key, value in dic.items():
    for x in key:
        print(x, end=' ')
    print()
