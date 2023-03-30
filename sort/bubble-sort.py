import random

# random 값이 20개 들어있는 배열 생성
rand_arr = []
for _ in range(20):
    rand_int = random.randrange(1, 100)
    while rand_int in rand_arr:
        rand_int = random.randrange(1, 100)
    rand_arr.append(rand_int)

print("정렬되기 전 배열: ", rand_arr)

def bubble_sort(arr_data: list) -> list:
    for i in range(len(arr_data)):
        for j in range(1, len(arr_data)-i):
            if arr_data[j] < arr_data[j-1]:
                arr_data[j], arr_data[j-1] = arr_data[j-1], arr_data[j]
            print(i,'번 round의 ', j, '번째: ', arr_data)
    
    return arr_data

sorted_arr = bubble_sort(rand_arr)
print(sorted_arr)
