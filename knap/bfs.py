n = 4
p = [40, 30, 50, 10, 0]
w = [2, 5, 10, 5, 0]
pw = [20, 6, 5, 2, 1]
tree = []
limit = 16
maxprofit = 0

class root:
    def __init__(self):
        self.profit = 0
        self.weight = 0
        self.cnt = [0, 0, 0, 0]
        self.bound = 0
        self.fail = 1

class branch:
    def __init__(self, parent, number):
        global n, limit
        self.profit = parent.profit
        self.weight = parent.weight
        self.parent = parent
        self.cnt = self.parent.cnt
        self.bound = 0
        self.fail = 1
    
    def knap(self, number, into):
        global p, w, pw
        self.cnt[number] = 1
        self.profit += p[number]*into
        self.weight += w[number]*into
        self.bound = self.bound_(number)

    def bound_(self, i):
        
        j=0
        k=0
        totweight=0
        if(w[i]>=limit):
            return 0
        else :
            j = i + 1
            self.bound = self.profit
            totweight=self.weight
            while(j<=n and totweight+w[j]<=limit):
                totweight = totweight + w[j]
                self.bound = self.bound + p[j]
                j = j + 1
            k=j
            if(k<=n):
                self.bound = self.bound + (limit - totweight)*(pw[k])
            if self.weight > limit or self.bound <= maxprofit:
                self.fail = 0


def main():
    global tree, maxprofit, limit, n
    zero = root()
    tree.append([zero])
    print(tree)
    maxnode = tree[0][0]
    for i in range(n):
        print("i = ", i)
        node = []
        for j in range(0, len(tree[i])):
            print()
            if tree[i][j].fail:
                node1 = branch(tree[i][j], i)
                node0 = branch(tree[i][j], i)
                node1.knap(i, 1)
                node0.knap(i, 0)
                print("node1 - ", node1.cnt)
                print("node0 - ", node0.cnt)
        tree.append(node)
        for j in tree[i+1]:
            if j.profit > maxprofit and j.weight <= limit:
                maxnode = j
    
    print(maxnode.profit)    
    print(maxnode.weight)
    print(maxnode.bound)
    print(maxnode.cnt)

main()