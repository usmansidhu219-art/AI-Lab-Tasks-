import heapq

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

h = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}


def search(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}

    processed = []
    expansion_count = 0

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if g != best[node]:
            continue

        if node == goal:
            total = sum(
                graph[path[i]][
                    next(j for j, edge in enumerate(graph[path[i]])
                         if edge[0] == path[i + 1])
                ][1]
                for i in range(len(path) - 1)
            )

            return path, total, processed, expansion_count

        processed.append(node)
        expansion_count += 1

        for nxt, w in graph[node]:
            new_g = g + w

            if new_g < best.get(nxt, float("inf")):
                best[nxt] = new_g
                new_f = new_g + h[nxt]

                heapq.heappush(
                    pq,
                    (new_f, new_g, nxt, path + [nxt])
                )

    return None, None, processed, expansion_count



astar_result = search(graph, h, "S", "G")


zero_h = {node: 0 for node in graph}
ucs_result = search(graph, zero_h, "S", "G")


print("A* Result:")
print("Path:", astar_result[0])
print("Path Cost:", astar_result[1])
print("Processed Nodes:", astar_result[2])
print("Expansion Count:", astar_result[3])

print("\nUCS Result:")
print("Path:", ucs_result[0])
print("Path Cost:", ucs_result[1])
print("Processed Nodes:", ucs_result[2])
print("Expansion Count:", ucs_result[3])
