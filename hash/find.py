n = int(input())
n_num = list(map(int, input().split()))

h = [0] * n
for i in n_num:
    h[i % n] = i

m = int(input())
m_num = list(map(int, input().split()))

for i in m_num:
    if (h[i % m] in m_num):
        print(1)
    else:
        print(0)