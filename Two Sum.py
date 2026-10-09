arr = [2, 7, 11, 15]
target = 9
seen = {}

for i, n in enumerate(arr):
    diff = target - n
    if diff in seen:
        print([seen[diff], i])
        break
    seen[n] = i