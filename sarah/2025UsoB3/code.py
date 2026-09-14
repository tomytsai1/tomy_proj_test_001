import sys
sys.stdin = open(r"C:\Users\samue\USACO Coding\test.in", "r")
length, num_queries = map(int, input().split())
contest = input()
# for i in range(len(contest)):
#     char = contest[i]
#     if char not in char_dict:
#         char_dict[char] = []
#     char_dict[char].append(i)
# put queries into a dictionary
queries = []
for i in range(num_queries):
    query = tuple(map(int, input().split()))
    new_query = (query[0] - 1, (query[0] + query[1] - 2) // 2, query[1] - 1)
    queries.append(new_query)
# sort queries based on their starting index
sorted_queries = sorted(queries)
char_dict = {}
active_queries = set()
different_chars = []
query_triplets = {}
j = 0
# put queries into a dictionary and in each of the values list out the different characters
# determine the triplets of each of the characters based on the current index
# in the end each value should have all the characters in the range along with their triplets
for i in range(len(contest)):
    char = contest[i]
    if char not in char_dict:
        different_chars.append(char)
        char_dict[char] = []
    char_dict[char].append(i)
    while j < num_queries and sorted_queries[j][0] == i:
        active_queries.add(sorted_queries[j])
        query_triplets[sorted_queries[j]] = {}
        for different_char in different_chars:
            query_triplets[sorted_queries[j]][different_char] = [-1, -1, -1]
            if different_char != char:
                query_triplets[sorted_queries[j]][different_char][0] = i
        j += 1
    print(query_triplets, active_queries)
    delete = []
    for query in active_queries:
        print(i, query)
        if char != contest[query[0]] and query_triplets[query][contest[query[0]]][0] == -1:
            query_triplets[query][contest[query[0]]][0] = i
        if char in query_triplets[query]:
            if i >= query[1] and query_triplets[query][char][1] == -1:
                query_triplets[query][char][1] = i
            query_triplets[query][char][2] = i
        if i == query[2]:
            delete.append(query)
    for query in delete:
        active_queries.remove(query)
print(query_triplets)

results = {}
for query in sorted_queries:
    current_max = -1
    for triplet in query_triplets[query].values():
        i, j, k = triplet
        # print(i, j, k)
        if j != k:
            first = (j - i) * (k - j)
        else:
            first = -1
        # if j > 0:
        #     second = (char_dict[char][] - i) * (k - indices[first_greater[char] - 1])
        # else:
        #     second = -1
        current_max = max(current_max, first)
    results[query] = current_max

for query in queries:
    print(results[query])
