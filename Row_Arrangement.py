def arrangeCoins(n):
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        total = (mid * (mid + 1)) // 2

        if total <= n:
            left = mid + 1
        else:
            right = mid - 1

    return right
n = int(input())
result = arrangeCoins(n)
print(result)
