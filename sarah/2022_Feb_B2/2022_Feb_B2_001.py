N = int(input())
original = list(map(int, input().split()))
goal = list(map(int, input().split()))
modifications = 0
moved = []
front = 0
for i in range(N):

    while original[front] in moved:
        front += 1

    if goal[i] != original[front]:
        modifications += 1
    moved.append(goal[i])
    front = 0
print(modifications)
