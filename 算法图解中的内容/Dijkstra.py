graph = {}
inifiity = float("inf")

"""start节点的邻居的cost"""
graph["start"] = {}
graph["start"]['a'] = 6
graph["start"]['b'] = 2

"""a节点的邻居的cost"""
graph["a"] = {}
graph['a']["fin"] = 1

"""b节点的邻居的cost"""
graph["b"] = {}
graph['b']['a'] = 3
graph['b']["fin"] = 5

"""fin节点的邻居的cost"""
graph["fin"] = {}

"""创建cost的散列表"""
costs = {}
costs["a"] = graph["start"]['a']
costs["b"] = graph["start"]['b']
costs["fin"] = inifiity

"""创建存贮父节点的散列表"""
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

"""用于记录处理过的节点"""
processed = []

def find_lower_cost_node(costs):
    """用于找到最低cost的节点"""
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


"""Dijkstra算法"""
node = find_lower_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lower_cost_node(costs)

print(parents)
print(costs)
