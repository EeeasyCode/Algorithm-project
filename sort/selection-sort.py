import numpy as np

# random 값이 20개 들어있는 배열 생성
# rand_arr = np.random.randint(1, 100, size = 20)
rand_arr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]

def selection_sort(arr_data: list) -> list:
    for i in range(len(arr_data)):
        max_index = 0
        for j in range(len(arr_data)-i):
            if arr_data[max_index] < arr_data[j]:
                max_index = j
        print(i, "번째 ", arr_data)        
        arr_data[max_index], arr_data[j] = arr_data[j], arr_data[max_index]
    return arr_data

print(selection_sort(rand_arr))






    
