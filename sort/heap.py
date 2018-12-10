import random
import time
li = []
exchange_count = 0
comparison_count = 0

def heap(end):
    global li
    global exchange_count
    global comparison_count
    while(end!=0):
        i = end
        while(i>0):
            parent = (i-1)//2

            # 자식 노드 갯수 파악
            if end % 2 == 0:
                # heap구조 체크
                comparison_count += 1
                if (li[parent] < li[i]) or (li[parent] < li[i-1]):
                        # heap 만족 못할 시 교환
                        comparison_count += 1
                        if li[i] > li[i-1]:
                            k = li[parent]
                            li[parent] = li[i]
                            li[i] = k
                            exchange_count += 1
                        elif li[i-1] > li[i]:
                            k = li[parent]
                            li[parent] = li[i-1]
                            li[i-1] = k
                            exchange_count += 1
                i -= 2
            else:
                # heap구조 체크
                comparison_count += 1
                if (li[parent] < li[i]):
                        # heap 만족 못할 시 교환
                        k = li[parent]
                        li[parent] = li[i]
                        li[i] = k
                i -= 1

        k = li[end]
        li[end] = li[0]
        li[0] = k
        end -= 1

# make list
n = int(input("How many samples do you want?"))
li = random.sample(range(1, 10000000), n)

# main function
st = time.time()
heap(len(li)-1)
end = time.time()

# result
print("result : \n", li)
print("time = ", end-st)
print("exchange count = ", exchange_count)
print("comparison count =", comparison_count)
