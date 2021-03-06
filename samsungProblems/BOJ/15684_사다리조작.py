# https://www.acmicpc.net/problem/15684

def check():
    for i in range(m):
        loc = i
        for j in range(n):
            if (loc-1 >= 0 and bridge[j][loc-1]):
                loc -= 1
            elif bridge[j][loc]:
                loc += 1
        if loc != i: return 0
    return 1
def solve(x, y, cnt):
    global res
    if cnt >= res: return
    if check():
        res = min(res, cnt)
        return
    for i in range(x, n):
        temp = y if x==i else 0
        for j in range(temp, m-1):
            if bridge[i][j]: continue
            bridge[i][j] = 1
            solve(i, j+2, cnt+1)
            bridge[i][j] = 0

#n * m 사각형, k개의 다리 정보 입력받을거
m, k, n = map(int,input().split())
bridge = [[0]*m for _ in range(n)]
for i in range(k):
    x, y = map(int,input().split())
    bridge[x-1][y-1] = 1
res = 4
solve(0, 0, 0)
print(res if res != 4 else -1)