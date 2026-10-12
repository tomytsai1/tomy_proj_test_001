n = int(input())
lineup = list(map(int, input().split()))
checkup = list(map(int, input().split()))
# not_satisfy = []
def check_satisfy():
    global reversed, checkup, not_satisfy
    count = 0
    # not_satisfy.clear()
    for i in range(n):
        if reversed[i] == checkup[i]:
            count += 1
            # not_satisfy.append(reversed[i])
    return count
result = [0 for _ in range(n + 1)]
for i in range(n):
    for j in range(i, n):
        # print(i, j)
        reversed = lineup[:i] + lineup[i:j + 1][::-1] + lineup[j + 1:]
        result[check_satisfy()] += 1
for r in result:
    print(r)
1 source
