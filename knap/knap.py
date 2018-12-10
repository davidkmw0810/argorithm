tree = []
item = []
limit = 0

class first:
    def __init__(self):
        self.profit = 0
        self.weight = 0
        self.li = [0, 0, 0, 0]
        self.fail = 1

class branch:

    def __init__(self, into, parents, depth):
        global item
        global tree
        if len(tree) == 0:
            self.profit = item[depth][0]*into
            self.weight = item[depth][1]*into
        else:
            self.profit = parents.profit + item[depth][0]*into
            self.weight = parents.weight + item[depth][1]*into

        self.li = parents.li
        self.li[depth] = into

        if self.weight > limit:
            self.fail = 0
        else:
            self.fail = 1

        print("class - node",str(into+1),".li = ", self.li)

        # self.bound = self.bound_(depth, item)

    # def bound_(self, depth, item):
    #     global limit
    #     j = 0
    #     k = 0
    #     totweight = 0

    #     if item[depth][1] >= limit:
    #         return 0
    #     else:
    #         j = depth + 1
    #         bound = self.profit
    #         totweight = self.profit
    #         while(k <= len(item) and totweight + item[k][1] <= limit):
    #             totweight += item[k][1]
    #             bound += item[k][0]
    #             j += 1
    #         k = j
    #         if(k<=len(item)):
    #             bound += (limit - totweight)*(item[k][0]/item[k][1])


def take():
    global tree
    num = int(input("how many item ? : "))

    for _ in range(num):
        profit, weight = input("profit and weight : ").split()
        profit = int(profit)
        weight = int(weight)
        item.append([profit, weight])
    limit = int(input("maximum weight :"))

    return num, limit


def main():
    global tree, item, limit
    num, limit = take()
    tree.append([first()])
    max = 0
    for i in range(0, num):
        l = []
        for j in range(0, len(tree[i])):
            parent = tree[i][j]
            if parent.fail == 1:
                node1 = branch(0, parent, i)
                node2 = branch(1, parent, i)
                print("===========")
                print("main - node1.li = ",node1.li)
                print("main - node2.li = ",node2.li)
                l.append(node1)
                l.append(node2)
                if node1.profit*node1.fail > max:
                    max_node = node1
                if node2.profit*node2.fail > max:
                    max_node = node1
        tree.append(l)
    print("--------------------")
    print(max_node.profit)
    print(max_node.weight)
    print(max_node.li)

main()