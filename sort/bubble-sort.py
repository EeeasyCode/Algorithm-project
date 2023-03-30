import tools

# random 값이 20개 들어있는 배열 생성
rand_arr = tools.make_random_arr(20)

print("정렬되기 전 배열: ", rand_arr)

#버블 정렬 알고리즘
def bubble_sort(arr_data: list) -> list:
    for i in range(len(arr_data)):
        for j in range(1, len(arr_data)-i):
            if arr_data[j] < arr_data[j-1]:
                arr_data[j], arr_data[j-1] = arr_data[j-1], arr_data[j]
    
    return arr_data

sorted_arr = bubble_sort(rand_arr)
print('정렬 후 배열: ', sorted_arr)
