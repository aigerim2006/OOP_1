def two_sum(arr, target_value):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target_value:
                return [i, j]
    return None

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

