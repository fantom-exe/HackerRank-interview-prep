def divisibleSumPairs(n, k, ar):
    pairs = 0

    for i in range(n-1):
        for j in range(i+1, n):
            num = ar[i] + ar[j]

            if num % k == 0:
                print('Pair: ', ar[i], '+', ar[j], '=', num)
                pairs += 1

    return pairs


ar = [1, 3, 2, 6, 1, 2]
n = 6
k = 3

print(divisibleSumPairs(n, k, ar))
