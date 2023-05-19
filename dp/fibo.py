memo_arr = []

def BU_fibo_DP(n:int) -> int:
    memo_arr.append(0)
    memo_arr.append(1)

    for i in range(2, n+1):
        memo_arr.append(memo_arr[i-1] + memo_arr[i-2])

    return memo_arr[-1]

print(BU_fibo_DP(5))

memo_arr = [0] * 50

def TD_fibo_DP(n:int) -> int:
    if n==1 or n==2:
        return 1
    
    if memo_arr[n] != 0:
        return memo_arr[n]
    
    memo_arr[n] = TD_fibo_DP(n-1) + TD_fibo_DP(n-2)        
    return memo_arr[n]

print(TD_fibo_DP(5))

