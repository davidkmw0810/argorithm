W = int(input("input the knapsack's weight limit : "))
tot_wei = 0 #지금 가방의 무게 / 초기값 0
n = int(input("input the number of goods : "))
pw = []
total_val = 0
get = [0, 0, 0, 0]
tries = 0
# goods = []
goods = [[40, 2], [30, 5], [50, 10], [10, 5]]  # 229쪽 예제. 테스트 케이스 이용시 이 줄 주석해제 및 윗줄 주석처리.[val,weight] 형태
# goods = [[50,5],[60,10],[140,20]]

#p/w 로 내림차순 정렬을 위하여 goods 배열 마지막에 각각 append 해줌.
for i in range(len(goods)):
    goods[i].append(goods[i][0]/goods[i][1])
goods.sort(reverse=True, key=lambda x: x[2]) #lamda를 이용한 정렬

#추가한 p/w 정보를 다시 삭제 : 정렬된 goods 리스트 완성.
for i in range(len(goods)):
    goods[i].remove(goods[i][-1])

#p/w 배열 만들기
for i in goods:
    pw.append(i[0]/i[1])
# print(pw)




def initialize():
    for i in range(0,n):
        n_val = int(input("Insert the price : "))
        n_wei = int(input("insert the weight : "))
        goods.append([n_val,n_wei])
        for i in goods:
            pw.append(i[0]/i[1])
    
# initialize()
def find_k(goods):
    res = 0
    k = 0
    for i in goods:
        res += i[1]
        if(res > W):
            k = goods.index(i)
    return k

def compute_totweight(goods, k):
    cnt = 0
    global tot_wei
    for i in goods:
        if cnt < k-1:
            tot_wei +=i[1]
            cnt += 1
    return tot_wei


def bound(i, pgoods):
    j = k = 0
    tot_wei = 0
    global tries
    tries += 1
    if(pgoods[1] > W):
        return 0
    else:
        j = i + 1
        bound = pgoods[0]
        tot_wei = pgoods[1]
        while (j<=n and tot_wei + pgoods[1] <= W):
            tot_wei += pgoods[1]
            bound += pgoods[0]
            j += 1
        k = j
        if(k<=n):
            bound += (W - tot_wei)*(pw[k-1])
        if(bound > total_val):
            return 1
        else:
            return 0
        
def knapsack(i,pgoods, cont): #goods[i]
    bestval = 0
    global total_val
    global get
    global goods
    # print(pgoods)
    
    if(i<=n):

        if(pgoods[1] <= W and pgoods[0] > total_val):
            total_val = pgoods[0]
            bestval = i
            get[goods.index(pgoods)] = 1
            
        if(bound(i, goods[i]) == 1):
            
            if(goods[i] in goods):
                pass
            else:
                get[goods.index(pgoods)] = 1
            knapsack(i+1, goods[i+1])
            knapsack(i+1, goods[i])
        print(get)
    return get
knapsack(0,goods[0])

        
def print_result():
    global tries
    global bound_arr
    
    for target in range(n):
        # print(target)
        if get[target]:
            print("item " + str(goods[target]) + " is selected.")
    print("The algorithm needs " + str(tries) + " nodes to search.") # 강제로 마지막2개 노드 연산한것을 제거하도록 했는데, 더 좋은방법 없나...

    # print(get)


print_result()