import random

# random 값이 20개 들어있는 배열 생성
rand_arr = []
for _ in range(20):
    rand_int = random.randrange(1, 100)
    while rand_int in rand_arr:
        rand_int = random.randrange(1, 100)
    rand_arr.append(rand_int)

print("정렬되기 전 배열: ", rand_arr)

#선택 정렬 알고리즘
def selection_sort(arr_data: list) -> list:
    for i in range(len(arr_data)-1):
        max_index = 0
        for j in range(1, len(arr_data)-i):
            if arr_data[max_index] < arr_data[j]:
                max_index = j
        arr_data[max_index], arr_data[j] = arr_data[j], arr_data[max_index]
    return arr_data

sorted_arr = selection_sort(rand_arr)

print("정렬 후 배열: ", sorted_arr)






    
