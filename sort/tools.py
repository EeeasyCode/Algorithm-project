import random

def make_random_arr(item_number: int) -> list:

    # random 값이 20개 들어있는 배열 생성
    rand_arr = []

    for _ in range(item_number):
        rand_int = random.randrange(1, 100)
        while rand_int in rand_arr:
            rand_int = random.randrange(1, 100)
        rand_arr.append(rand_int)

    print("정렬되기 전 배열: ", rand_arr)

    return rand_arr