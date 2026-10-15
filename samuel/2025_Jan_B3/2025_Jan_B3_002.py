import sys
import time
start = time.time()
sys.stdin = open(r"C:\Users\samue\USACO Coding\2025_Jan_B3\7.in")
n = int(input())
lineup = list(map(int, input().split()))
checkup = list(map(int, input().split()))
original_count = 0
for i in range(n):
    if lineup[i] == checkup[i]:
        original_count += 1
result = [0 for _ in range(n + 1)]
# odd reverses
for i in range(n):
    new_lineup = lineup.copy()
    current_count = original_count
    for radius in range(min(i, n - i - 1) + 1):
        if new_lineup[i - radius] == checkup[i - radius]:
            current_count -= 1
        if new_lineup[i + radius] == checkup[i + radius]:
            current_count -= 1
        new_lineup[i - radius], new_lineup[i + radius] = new_lineup[i + radius], new_lineup[i - radius]
        if new_lineup[i - radius] == checkup[i - radius]:
            current_count += 1
        if new_lineup[i + radius] == checkup[i + radius]:
            current_count += 1
        result[current_count] += 1
# even reverses
for i in range(1, n):
    new_lineup = lineup.copy()
    current_count = original_count
    for radius in range(min(i - 1, n - i - 1) + 1):
        if new_lineup[i - radius - 1] == checkup[i - radius - 1]:
            current_count -= 1
        if new_lineup[i + radius] == checkup[i + radius]:
            current_count -= 1
        # print(new_lineup, min(i - 1, n - i - 1), i, radius)
        new_lineup[i - radius - 1], new_lineup[i + radius] = new_lineup[i + radius], new_lineup[i - radius - 1]
        if new_lineup[i - radius - 1] == checkup[i - radius - 1]:
            current_count += 1
        if new_lineup[i + radius] == checkup[i + radius]:
            current_count += 1
        result[current_count] += 1
for r in result:
    print(r)
end = time.time()
print(end - start)
# 7.in took 38.077773332595825 seconds
# 1-6 took 77 ms
