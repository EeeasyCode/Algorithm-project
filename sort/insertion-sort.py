import random

# random 값이 20개 들어있는 배열 생성
rand_arr = []
for _ in range(20):
    rand_int = random.randrange(1, 100)
    while rand_int in rand_arr:
        rand_int = random.randrange(1, 100)
    rand_arr.append(rand_int)

print("정렬되기 전 배열: ", rand_arr)

#삽입 정렬 알고리즘
def insertion_sort(arr_data: list) -> list:
    for i in range(len(arr_data)):
        for j in range(i, 0, -1):
            if arr_data[j] < arr_data[j-1]:
                arr_data[j], arr_data[j-1] = arr_data[j-1], arr_data[j]
    return arr_data

sorted_arr = insertion_sort(rand_arr)
print("정렬 후 배열: ", sorted_arr)
