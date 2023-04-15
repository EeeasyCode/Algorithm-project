# 2023 - 1 알고리즘 실습 과제

## Programming Languege

> python3

## Algorithm

### 기본 정렬 알고리즘
- Selection Sort
> 가장 큰 수를 찾아 정렬되어 있지 않은 부분의 마지막 원소와 swap <br>
> 최악의 경우 수행시간 : O(n2) <br>
> 평균 수행시간 : O(n2) <br>
> 최선의 경우 수행시간 : O(n2) <br>
> 비교횟수 : n(n-1)/2 <br>
> 안정성 : X <br>

- Bubble Sort
> 인접한 두 원소의 대소 비교 후, 왼쪽 원소가 더 크면 swap 하는 방식으로 정렬 <br>
> 최악의 경우 수행시간 : O(n2) <br>
> 평균 수행시간 : O(n2) <br>
> 최선의 경우 수행시간 : O(n2) <br>
> 비교횟수 : n(n-1)/2 <br>
> 안정성 : O <br>

- Insertion Sort
> 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교 하여, 자신의 위치를 찾아 삽입함으로써 정렬 -> 삽입 시, 자신보다 큰 수는 오른쪽으로 한칸씩 이동
> 최악의 경우 수행시간 : O(n2) <br>
> 평균 수행시간 : O(n2) <br>
> 최선의 경우 수행시간 : O(n) <br> -> 이때 최선의 경우는 배열이 전부 정렬되어 있거나 거의 정렬이 되어있을 경우
> 평균 비교횟수 : n(n-1)/2 <br>
> 최선 비교횟수 : n-1 <br> 
> 안정성 : O <br>

### 고급 정렬 알고리즘
- Merge Sort
> 주어진 배열을 원소가 하나 밖에 남지 않을 때까지 계속 분할한 후에 다시 재배열 하면서 정렬 <br>
> 평균 수행시간 : O(nlogn) <br>
> 안정성 : O <br>

- Heap Sort
> 힙이라는 특수한 형태의 자료구조를 사용하여 정렬 <br>
> heap build : O(n) <br>
> heapify : O(logn) <br>
> 평균 수행시간 : O(nlogn) <br>
> 안정성 : X <br>

- Quick Sort
> 기준원소를 사용하여, 기준원소보다 작은 원소와 큰 원소를 나누어 정렬 <br>
> 최선의 경우 수행시간 : O(nlogn) <br>
> 최악의 경우 수행시간 : O(n2) -> 분할 과정에서 계속 한쪽으로만 몰리는 경우 (이미 정렬되어 있는 배열) <br>
> 안정성 : X <br>

### 특수 정렬 알고리즘
- 기수 정렬
> 원소가 k자리수 이하인 특수한 경우에 사용 <br>
> 각 자리수를 이용하여 정렬 <br>
> 평균 수행시간 : O(n) <br>

- 계수 정렬
> 주어진 배열의 값 범위가 작은 경우 빠른 속도를 갖는 정렬 알고리즘. 최댓값과 입력 배열의 원소 값 개수를 누적합으로 구성한 배열로 정렬 <br>
> 평균 수행시간 : O(n) <br>

### 이진 탐색 트리
- 속성
> 1. 이진 검색 트리의 각 노드는 하나의 Key를 갖음 <br>
> 2. 각 노드의 Key 값은 서로 달라야 함 <br>
> 3. 최상위 Level에 Root 노드가 있고, 각 노드는 최대 두 개의 자식 노드를 갖음 <br>
> 4. 임의의 노드의 Key 값은 자신의 왼쪽에 있는 모든 노드의 Key 값도다 크고, 오른쪽에 있는 모든 노드의 Key 값보다 작음 <br>

- 검색
> Root 노드부터 시작하여, 찾고자하는 원소의 값과 노드의 Key 값을 비교하며 탐색 <br>
> 임의의 Leaf 노드까지 도달하게 되면, NULL <br>

- 삽입
> Root 노드부터 시작하여, 삽입하고자 하는 원소의 값과 노드의 Key 값을 비교하며 탐색 <br>
> 임의의 Leaf 노드의 자식 노드가 NULL이면, 그 곳에 삽입 <br>

- 삭제
> Case 1 : 삭제 노드가 리프 노드일 경우 <br>
> Case 2 : 삭제 노드의 자식 노드가 1개일 경우 <br>
> Case 3 : 삭제 노드의 자식 노드가 2개일 경우 <br>

``` 
treeDelete(t, r, p) {
// t: 트리의 루트노드를 함수에 건네서, 트리를 전달한다.
// r: 삭제하고자 하는 Key
// p: r의 부모 노드

    if(r == t)   // r이 루트 노드인 경우
    	then root ← deleteNode(t);
    else if(r == left[p])   // r이 p의 왼쪽 자식인 경우
    	then left[p] ← deleteNode(r);
    else   // r이 p의 오른쪽 자식인 경우
    	right[p] ← deleteNode(r);
}

deleteNode(r) {
    if(left[r] == right[r] == NULL)   // Case I
        then return NULL;
    else if (left[r] == NULL and right[r] != NULL)   // Case II
        then return right[r];
    else if (left[r] != NULL and right[r] == NULL)   // Case II
        then return left[r];
    else {   // Case III
        s ← right[r]; // r의 오른쪽 자식들중에서
        while(left[s] != NULL) {  // 가장 작은 Key를 가진 노드를 찾아간다. (왼쪽 Link로만 계속 타고 내려가면 r의 오른쪽 Subtree에서 가장 작은 노드를 찾을 수 있다.
            parent ← s;
            s ← left[s];
        }
        key[r] ← key[s];
        if (s == right[r])
            then right[r] ← right[s];
        else
            left[parent] ← right[s];
        return r;
    }
}
```

