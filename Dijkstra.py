# -*- coding: utf-8 -*-


def dijkstra_algor(src, adjacent_table):
    # initialize
    last_visited = src
    node_list = adjacent_table.keys()  # all nodes' list
    unvisited = set(node_list) - {last_visited}
    d = {node: float('inf') for node in node_list}     # store min distance
    # r = {node: list() for node in node_list}  # store min route
    for node in adjacent_table[src].keys():
        d[node] = adjacent_table[src][node]
    d[src] = 0

    # find next one
    while unvisited:
        # update distance
        min_value, min_node = float('inf'), None
        for c in unvisited:
            if c in adjacent_table[last_visited].keys():
                if d[c] >= d[last_visited]+adjacent_table[last_visited][c]:
                    d[c] = d[last_visited]+adjacent_table[last_visited][c]
                    # r[c] = r[last_visited]+[(last_visited, c)]
            if d[c] <= min_value:
                min_value, min_node = d[c], c
        unvisited.remove(min_node)
        last_visited = min_node
    return d





