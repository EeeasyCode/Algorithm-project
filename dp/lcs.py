# a = input()
# b = input()

# a_len = len(a) + 1
# b_len = len(b) + 1

# arr = [[0for _ in range(a_len)] for _ in range(b_len)]

# for i in range(1, b_len):
#     for j in range(1, a_len):
#         if a[j-1] == b[i-1]:
#             arr[i][j] = arr[i-1][j-1] + 1
#         else:
#             arr[i][j] = max(arr[i-1][j], arr[i][j-1])


# print(arr[-1][-1])
# s = arr[-1][-1]
# answer = ''
# y, x = len(arr) - 1, len(arr[0]) - 1

# while s!=0:
#     if arr[y][x-1] == s-1 and arr[y-1][x] == s-1:
#         answer = a[x-1] + answer
#         s -= 1
#         x -= 1
#         y -= 1
#     else:
#         if arr[y-1][x] > arr[y][x-1]:
#             y -= 1
#         else:
#             x -= 1

# print(answer)
            


n = input()
m = input()

n_len = len(n) + 1
m_len = len(m) + 1
arr = [[0 for _ in range(n_len)] for _ in range(m_len)]

for i in range(1, m_len):
    for j in range(1, n_len):
        if n[j-1] == m[i-1]:
            arr[i][j] = arr[i][j-1] + 1
        else:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])

print(arr[-1][-1])

                      

