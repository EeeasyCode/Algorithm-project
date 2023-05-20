# n = int(input())
# n_num = list(map(int, input().split()))

# h = [0] * n
# for i in n_num:
#     h[i % n] = i

# m = int(input())
# m_num = list(map(int, input().split()))

# for i in m_num:
#     if (h[i % m] in m_num):
#         print(1)
#     else:
#         print(0)

# dict 사용
from collections import Counter

n = int(input())
arr1 = map(int, input().split())
arr1 = Counter(arr1)

m = int(input())
arr2 = map(int, input().split())

for num in arr2:
    if num in arr1:
        print('1')
    else:
        print('0')

# set 사용
n = int(input())
arr1 = map(int, input().split())
arr1 = set(arr1)

m = int(input())
arr2 = map(int, input().split())

for num in arr2:
    if num in arr1:
        print('1')
    else:
        print('0')