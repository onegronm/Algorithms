# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    # create color frequency array
    color_count = [0] * 101

    for i in ar:
        color_count[i] += 1

    color_count_index = 0
    pair_count = 0

    while color_count_index < len(color_count):
        pair_count += color_count[color_count_index] // 2 # floor division in Python 3. It rounds down to the nearest integer.
        color_count_index += 1

    return pair_count;


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(n, ar))