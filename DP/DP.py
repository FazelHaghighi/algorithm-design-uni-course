def min_jumps_path(arr):
    n = len(arr)
    jumps = [float("inf")] * n
    path = [-1] * n

    if not n or not arr[0] or all(x == 0 for x in arr):
        return "Unreachable!", []

    jumps[0] = 0

    for i in range(1, n):
        for j in range(i):
            if j + arr[j] >= i and jumps[j] != float("inf"):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                if jumps[i] == jumps[j] + 1:
                    path[i] = j

    if jumps[-1] == float("inf"):
        return "Unreachable!", []

    actual_path = []
    i = n - 1
    while i != -1:
        actual_path.append(arr[i])
        i = path[i]

    return jumps[-1], actual_path[::-1]

GREEN = '\033[92m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RED = '\033[91m'
MAGENTA = '\033[95m'
YELLOW = '\033[93m'
END = '\033[0m'

arr = [4, 3, 1, 2, 0, 4, 3, 2, 1]
jumps, path = min_jumps_path(arr)

if jumps == "Unreachable!":
    print(f"{RED}The end point is unreachable.{END}")
else:
    print(f"{CYAN}The minimum number of jumps required to reach the end point is {jumps}.{END}")
    print(f"{MAGENTA}The path is:{END}")
    print(f"{YELLOW} -> {END}".join(f"{BLUE}{p}{END}" for p in path))

# [2, 1, 4, 1, 3, 4, 2, 1, 1, 1, 0, 6]
# [1, 3, 5, 8, 9, 12, 1, 5, 10, 8, 9]
