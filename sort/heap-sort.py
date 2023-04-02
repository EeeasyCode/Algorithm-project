import tools

# random 값이 20개 들어있는 배열 생성
rand_arr = tools.make_random_arr(20)

def heapify(rand_arr:list, arr_size:int):
    p = (arr_size // 2) 
    while p >= 0:
        shiftdown(rand_arr, p, arr_size)
        p -= 1

def shiftdown(a: list, p:int, size:int):
    left_child = p*2 + 1
    right_child = p*2 + 2
    smallest = p

    if (left_child <= size and a[left_child] < a[smallest]):
        smallest = left_child
    if (right_child <= size and a[right_child] < a[smallest]):
        smallest = right_child
    if (smallest != p):
        a[smallest], a[p] = a[p], a[smallest]
        shiftdown(a, smallest, size)

heapify(rand_arr, len(rand_arr)-1)
sorted_arr=[]
for i in range(len(rand_arr)-1, 0, -1):
    rand_arr[i], rand_arr[0] = rand_arr[0], rand_arr[i]
    sorted_arr.append(rand_arr.pop())
    heapify(rand_arr, len(rand_arr)-1)
sorted_arr.append(rand_arr.pop())

print(sorted_arr)
