import sys
sys.stdin = open(r"C:\Users\samue\USACO Coding\2025_Open_B3\1.in", "r")
n, q = map(int, input().split())
contest = input()
left = [[-1] * 26 for _ in range(n)]
right = [[n] * 26 for _ in range(n)]
not_right = [[n] * 26 for _ in range(n)]
for i in range(n):
    c = contest[i]
    if i:
        left[i] = left[i - 1][:]
    left[i][ord(c) - ord('a')] = i
print(left)
for i in range(n - 1, -1, -1):
    c = contest[i]
    if i + 1 < len(contest):
        right[i] = right[i + 1][:]
    right[i][ord(c) - ord('a')] = i
    best = n
    second_best = n
    for j in range(26):
        if right[i][j] < best:
            second_best = best
            best = right[i][j]
        elif right[i][j] < second_best:
            second_best = right[i][j]
    for j in range(26):
        if right[i][j] == best:
            not_right[i][j] = second_best
        else:
            not_right[i][j] = best
