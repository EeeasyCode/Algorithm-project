memo_arr = []

def fibo_DP(n:int) -> int:
    memo_arr.append(0)
    memo_arr.append(1)

    for i in range(2, n+1):
        memo_arr.append(memo_arr[i-1] + memo_arr[i-2])
    
    return memo_arr[-1]

print(fibo_DP(5))
