import sys
sys.stdin = open('9.in', 'r')
# sys.stdout = open('lineup.out', 'w')
pairs = {}
leftover = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
# what is left to add to the current order
index = [0, 0, 0, 0, 0, 0, 0, 0]
for _ in range(int(input())):
    x, y = input().split(" must be milked beside ")
    if x not in pairs:
        pairs[x] = y
    else:
        pairs[y] = x
others = pairs.values()        
# print(pairs, others)
# The index you take from the "leftover" list (last index has to be 0
# because only one name will be left)
l = 7
# l is the level(index) of index
out = []
# current order
lsts = []
# store the outs that are legal
count = 0
# temporary var to keep track of # of complete rounds
dir_left = False
# is "l" currently traversing in the left direction
while True:
    
    # check if one round is complete
    if l == 7:
        count += 1
        out = []
        dir_left = True
        l -= 1
        # print(index)
        for i in range(8):
            out.append(leftover[index[i]])
            leftover.pop(index[i])
        # print(out)
        leftover = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
        check = True
        prev = ""
        for ind, cow in enumerate(out):
            try:
                if ind == 7:
                    ind = 6
                if prev != pairs[cow] and out[ind + 1] != pairs[cow]:
                    check = False
                    break
                # else:
                #     print(out)
                prev = cow
            except:
                if cow in others:
                    try:
                        if pairs[prev] != cow:
                            check = False
                            break
                    except:
                        prev = cow
                prev = cow
            
            # not working, trying to compare previous with current but something's wrong
            # too many try's and if's
        if check == True:
            for cow in out:
                print(cow)
            break
        # if out[0] == "Beatrice":
        #     print(out)
            
        
    if l <= -1:
        # print(count)
        break
    
    if dir_left == True:
        if index[l] + 1 <= 7 - l:
            index[l] += 1
            l += 1
            dir_left = False
            l = 7

        else:
            index[l] = 0
            l -= 1
