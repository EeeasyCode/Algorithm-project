import tools

# random 값이 20개 들어있는 배열 생성
rand_arr = tools.make_random_arr(20)

def partition(arr_data:list, start:int, end:int):
    i = start
    pivot_data = arr_data[end]
    for j in range(start, end):
         if (arr_data[j] <= pivot_data):
               arr_data[i], arr_data[j] = arr_data[j], arr_data[i]
               i+=1
    arr_data[i], arr_data[end] = arr_data[end], arr_data[i]
    return arr_data.index(pivot_data)
        

def quick_sort(arr_data:list, p:int, r:int):
    if (p < r):
            q = partition(arr_data, p, r)
            quick_sort(arr_data, p, q-1)
            quick_sort(arr_data, q+1, r)

quick_sort(rand_arr, 0, len(rand_arr)-1)
print(rand_arr)
    
