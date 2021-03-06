# https://www.acmicpc.net/problem/14499
dice = [0] * 6
#방향 변화, 0:위, 1:뒤, 2:오, 3:왼, 4:앞, 5:아래
changeDirection = [[],
                   [3, 1, 0, 5, 4, 2],      #동쪽
                   [2, 1, 5, 0, 4, 3],      #서쪽
                   [4, 0, 2, 3, 5, 1],      #북쪽
                   [1, 5, 2, 3, 0, 4]]      #남쪽
dd = [0,(0, 1), (0, -1), (-1, 0), (1, 0)]   #1부터 동서남북
n, m, x, y, k = map(int, input().split())
board=[[0]*m for _ in range(n)]
for i in range(n):
    tempInput = list(map(int, input().split()))
    for j in range(m):
        board[i][j] = tempInput[j]
moveCommands = list(map(int, input().split()))
for command in moveCommands:
    dx, dy = dd[command]
    nx, ny = x+dx, y+dy
    if nx<0 or ny<0 or nx>n-1 or ny>m-1: continue
    tempDice = [0]*6
    for i in range(6):
        tempDice[i] = dice[changeDirection[command][i]]
    for i in range(6):
        dice[i] = tempDice[i]
    if not board[nx][ny]:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    print(dice[0])
    x, y = nx, ny

