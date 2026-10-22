# import sys
# sys.stdin = open(r"C:\Users\samue\USACO Coding\2025_Jan_B1\3.in")
def main():
    n = int(input())
    for _ in range(n):
        size, right, down = map(int, input().split())
        photo = []
        for r in range(size):
            row = input()
            photo.append([])
            for c in range(size):
                photo[r].append(row[c])
        print(num_stars(size, right, down, photo))
def num_stars(size, right, down, photo):
    stars = set()
    for r in range(size):
        for c in range(size):
            # print((r, c), photo)
            if photo[r][c] == "G":
                if r - down >= 0 and c - right >= 0 and photo[r - down][c - right] == "B":
                    continue
                if r + down < size and c + right < size and photo[r + down][c + right] in "BG":
                    stars.add((r, c))
                    continue
                if r - down >= 0 and c - right >= 0 and photo[r - down][c - right] == "G":
                    if (r - down, c - right) not in stars:
                        stars.add((r - down, c - right))
                    continue
                # print((r, c))
                stars.add((r, c))
            if photo[r][c] == "B":
                if r - down >= 0 and c - right >= 0:
                    if photo[r - down][c - right] in "BG":
                        stars.add((r, c))
                        continue
                # print((r, c), right, down, size)
                return -1
    # print(stars)
    return len(stars)
main()
