import random
import time
li = []
exchange_count = 0
comparison_count = 0

def quick(st, end):
    global li
    global exchange_count
    global comparison_count
    pivot = li[st]
    left = st
    right = end

    comparison_count += 1
    while(left != right):
        comparison_count += 1
        while(left != right):
            comparison_count += 1
            if li[right] < pivot:
                li[left] = li[right]
                exchange_count += 1
                break
            right -= 1

        while(left != right):
            comparison_count += 1
            if li[left] > pivot:
                li[right] = li[left]
                exchange_count += 1
                break
            left += 1

    li[left] = pivot
    exchange_count += 1
    if st != left:
        quick(st, left-1)
    if end != right:
        quick(right+1, end)

# make list
n = int(input("How many samples do you want?"))
li = random.sample(range(1, 10000000), n)

# 인덱스 번호로 호출
st = time.time()
quick(0, len(li) - 1)
end = time.time()

# sort 결과 출력
print("result : \n", li)
print("time = ", end-st)
print("exchange count = ", exchange_count)
print("comparison count = ", comparison_count)