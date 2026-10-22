# import sys
# sys.stdin = open(r"C:\Users\samue\USACO Coding\2025_Jan_B1\1.in")
def main():
    n = int(input())
    for _ in range(n):
        size, right, down = map(int, input().split())
        photo = []
        for r in range(size):
            row = input()
            photo.append(row)
        print(num_stars(size, right, down, photo))
def num_stars(size, right, down, photo):
    stars = set()
    cannot_use = set()
    for r in range(size):
        for c in range(size):
            # print(stars)
            if photo[r][c] == "G":
                if r + down < size and c + right < size and photo[r + down][c + right] == "B":
                    stars.add((r, c))
                    cannot_use.add((r + down, c + right))
                    continue
                if r - down >= 0 and c - right >= 0 and photo[r - down][c - right] == "B":
                    continue
                if (r - down, c - right) not in cannot_use:
                    if r - down >= 0 and c - right >= 0 and photo[r - down][c - right] == "G":
                        if (r - down, c - right) not in stars:
                            stars.add((r - down, c - right))
                            cannot_use.add((r, c))
                        continue
                if r + down < size and c + right < size and photo[r + down][c + right] == "G":
                    stars.add((r, c))
                    cannot_use.add((r + down, c + right))
                stars.add((r, c))
            if photo[r][c] == "B":
                if r - down >= 0 and c - right >= 0 and photo[r - down][c - right] in "BG":
                    stars.add((r, c))
                    continue
                return -1
    # print(stars)
    return len(stars)
main()
