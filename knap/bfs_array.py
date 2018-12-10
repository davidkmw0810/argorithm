
# n = 4
# p = [40, 30, 50, 10, 0]
# w = [2, 5, 10, 5, 0]
# pw = [20, 6, 5, 2, 0]
# limit = 16

# exercise #1
n = 5
p = [20, 30, 35, 12, 3, 0]
w = [2, 5, 7, 3, 1, 0]
pw = [10, 6, 5, 4, 3, 0]
limit = 13

tree = []
maxprofit = 0
maxnode = []
 # tree[depth][node_number][0.profit, 1.weight, 2.inout_list, 3.bound, 4.fail, 5.node_number, 6.level]

def make_node(inout, parent, depth, node_num):
    global n, p, w, pw, limit
    profit = parent[0] + p[depth]*inout
    weight = parent[1] + w[depth]*inout
    inout_list = parent[2]
    inout_list[depth] = inout
    node = [profit, weight]
    node.append([0]*n)
    for i in range(n):
        node[2][i] = inout_list[i]

    bound = find_bound(node, depth)
    node.append(bound)

    # fail
    if weight > limit or bound <= maxprofit:
        node.append(0)
    else:
        node.append(1)
    node.append(node_num)
    node.append(depth)
    return node

def find_bound(node, depth):
    global n, p, w
    profit = node[0]
    weight = node[1]
    k=n
    for i in range(depth+1, n):
        if weight + w[i] > limit:
            k = i
            break
        else:
            weight += w[i]

    weight = node[1]
    for i in range(depth+1, k):
        profit += p[i]
        weight += w[i]
    if limit<weight:
        bound = 0
    else:
        bound = profit + (limit - weight)*pw[k]

    return bound

def main():
    global n, p, w, pw, limit, maxprofit, tree
    # make zero_node
    node_num = 1
    tree.append([[0, 0, [0]*n, find_bound([0, 0, [0]*n], -1)]])
    tree[0][0].append(1)
    tree[0][0].append(node_num)
    i = 0
    
    while (i <= len(tree)-1 and i < n):
        session = tree[i]
        node_list = []
        for j in range(len(session)):
            if session[j][4] == 1:

                node_in = make_node(1, session[j], i, node_num+1)
                if node_in[0] >= maxprofit and node_in[4] == 1:
                    maxprofit = node_in[0]
                    maxnode = node_in

                node_out = make_node(0, session[j], i, node_num+2)
                if node_out[0] >= maxprofit and node_out[4] == 1:
                    maxprofit = node_out[0]
                    maxnode = node_out
                
                node_num += 2
                node_list.append(node_in)
                node_list.append(node_out)
            else:
                pass
        tree.append(node_list)
        i += 1

    # print("information of node")
    # for i in tree:
    #     for j in range(len(i)):
    #         print("node ", i[j][5], " = ", i[j])

    print("maxprofit = ", maxprofit)
    print("max_node : profit : {0}\n           weight : {1}\n           inout_list : {2}\n           bound : {3}\n           node_number : {4}\n           level : {5}".format(maxnode[0], maxnode[1], maxnode[2], maxnode[3], maxnode[5], maxnode[6]))

main()
