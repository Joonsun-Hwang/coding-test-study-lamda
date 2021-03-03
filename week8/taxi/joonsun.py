from collections import defaultdict
import heapq

def build_graph(fares):
    graph = defaultdict(dict)
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]
    return graph

def dijkstra(n, start, graph):
    s_idx = start-1
    
    pq = [(0, s_idx)]
    costs = {vertex: 1000000 for vertex in range(n)}
    costs[s_idx] = 0
    
    while len(pq) > 0:
        current_cost, current_idx = heapq.heappop(pq)
        if current_cost > costs[current_idx]:
            continue
            
        current_vertex = current_idx+1
        for neighbor, weight in graph[current_vertex].items():
            neighbor_idx = neighbor-1
            cost = current_cost + weight
            if cost < costs[neighbor_idx]:
                costs[neighbor_idx] = cost
                heapq.heappush(pq, (cost, neighbor_idx))

    return costs

def find_cost(n, s, a, b, graph):
    s_idx = s-1
    each_costs = {}
    for (k_a, v_a), (k_b, v_b) in zip(dijkstra(n, a, graph).items(), dijkstra(n, b, graph).items()):
        assert k_a == k_b
        each_costs[k_a] = v_a + v_b
    
    print(each_costs)
    
    ab_costs = {}
    for each_idx, each_cost in each_costs.items():
        if each_cost < 2000000:
            ab_costs[each_idx] = each_cost + dijkstra(n, each_idx+1, graph)[s_idx]
    
    return min(ab_costs.values())

def solution(n, s, a, b, fares):
    
    graph = build_graph(fares)
    return find_cost(n, s, a, b, graph)

