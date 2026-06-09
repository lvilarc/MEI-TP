#!/usr/bin/env python3

import sys
from collections import defaultdict


def read_graph():
    lines = [line.strip() for line in sys.stdin if line.strip()]

    if not lines:
        sys.exit("Error: empty input")

    first = lines[0].split()
    if len(first) != 2:
        sys.exit("Error: first line must contain: n r")

    try:
        n = int(first[0])
    except ValueError:
        sys.exit("Error: n must be an integer")

    root = first[1]

    adjacency_sets = defaultdict(set)

    # If vertices are labelled a, b, c, ..., initialise them from n.
    # This also allows isolated vertices to appear in the output.
    if len(root) == 1 and root.isalpha() and n <= 26:
        for i in range(n):
            v = chr(ord("a") + i)
            adjacency_sets[v]

    adjacency_sets[root]

    for line in lines[1:]:
        parts = line.split()
        if len(parts) != 2:
            sys.exit(f"Error: invalid edge line: {line}")

        u, v = parts
        adjacency_sets[u].add(v)
        adjacency_sets[v].add(u)

    graph = {
        vertex: sorted(neighbours)
        for vertex, neighbours in adjacency_sets.items()
    }

    return n, root, graph


def add_vertices_from_edge(component, seen, edge):
    parent, child = edge

    # Add child before parent to match DFS tree edge pop order.
    for vertex in (child, parent):
        if vertex not in seen:
            component.append(vertex)
            seen.add(vertex)


def compute_dfs_data(graph, root):
    vertices = sorted(graph.keys())

    discovery = {}
    low = {}
    parent = {}
    height = {}
    articulation = {v: False for v in vertices}

    tree_edge_stack = []
    biconnected_components = []

    time = 0

    def pop_component_until(target_edge):
        component = []
        seen = set()

        while tree_edge_stack:
            edge = tree_edge_stack.pop()
            add_vertices_from_edge(component, seen, edge)

            if edge == target_edge:
                break

        if component:
            biconnected_components.append(component)

    def dfs(u):
        nonlocal time

        discovery[u] = time
        low[u] = time
        time += 1

        child_count = 0
        root_child_edges = []

        for v in graph[u]:
            if v not in discovery:
                parent[v] = u
                height[v] = height[u] + 1

                tree_edge = (u, v)
                tree_edge_stack.append(tree_edge)

                if parent[u] == u:
                    root_child_edges.append(tree_edge)

                child_count += 1
                dfs(v)

                low[u] = min(low[u], low[v])

                if parent[u] != u and low[v] >= discovery[u]:
                    articulation[u] = True
                    pop_component_until(tree_edge)

            elif v != parent[u]:
                low[u] = min(low[u], discovery[v])

        if parent[u] == u:
            if child_count > 1:
                articulation[u] = True

            # For DFS roots, pop root-child components after all children
            # have been explored. This gives deterministic component order.
            for edge in reversed(root_child_edges):
                pop_component_until(edge)

    # Start with the requested root.
    if root not in graph:
        graph[root] = []
        vertices = sorted(graph.keys())

    parent[root] = root
    height[root] = 0
    dfs(root)

    # If the graph is disconnected, continue DFS on the remaining vertices.
    for v in vertices:
        if v not in discovery:
            parent[v] = v
            height[v] = 0
            dfs(v)

    return parent, height, articulation, biconnected_components


def print_graph(graph):
    print("Graph:")
    for vertex in sorted(graph.keys()):
        neighbours = ", ".join(graph[vertex])
        if neighbours:
            print(f"[{vertex}]: {neighbours}")
        else:
            print(f"[{vertex}]:")
    print()


def print_vertex_map(title, data, vertices):
    print(title)
    for vertex in vertices:
        print(f"[{vertex}]: {data[vertex]}")
    print()


def print_components(components):
    print("Biconnected Components")
    for component in components:
        print("{" + ", ".join(component) + "}")


def main():
    sys.setrecursionlimit(100000)

    _, root, graph = read_graph()

    parent, height, articulation, components = compute_dfs_data(graph, root)

    vertices = sorted(graph.keys())

    print_graph(graph)
    print_vertex_map("Parent", parent, vertices)
    print_vertex_map("Height", height, vertices)
    print_vertex_map("Articulation Points", articulation, vertices)
    print_components(components)


if __name__ == "__main__":
    main()