import sys
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    root = input_data[idx]; idx += 1

    graph = defaultdict(list)
    vertices = set()

    while idx + 1 < len(input_data):
        u = input_data[idx]; idx += 1
        v = input_data[idx]; idx += 1
        graph[u].append(v)
        graph[v].append(u)
        vertices.add(u)
        vertices.add(v)

    # Sort all adjacency lists alphabetically
    for v in graph:
        graph[v] = sorted(graph[v])

    sorted_vertices = sorted(vertices)

    # ── DFS setup ────────────────────────────────────────────────────────────
    sys.setrecursionlimit(10000)

    parent  = {}
    height  = {}
    disc    = {}   # discovery time
    low     = {}   # low value (for articulation points / BCCs)
    visited = set()
    ap_set  = set()
    timer   = [0]

    bcc_stack = []   # edge stack for biconnected components
    bcc_list  = []   # resulting biconnected components

    def dfs(u, par):
        visited.add(u)
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        child_count = 0

        for v in graph[u]:
            if v not in visited:
                child_count += 1
                parent[v] = u
                height[v] = height[u] + 1
                bcc_stack.append((u, v))
                dfs(v, u)
                low[u] = min(low[u], low[v])

                # Articulation point check
                is_root = (par == u)
                if is_root and child_count > 1:
                    ap_set.add(u)
                if not is_root and low[v] >= disc[u]:
                    ap_set.add(u)

                # Extract biconnected component when low[v] >= disc[u]
                if low[v] >= disc[u]:
                    component = set()
                    while True:
                        edge = bcc_stack.pop()
                        component.add(edge[0])
                        component.add(edge[1])
                        if edge == (u, v):
                            break
                    bcc_list.append(component)

            elif v != par and disc[v] < disc[u]:
                # Back edge
                bcc_stack.append((u, v))
                low[u] = min(low[u], disc[v])

    parent[root] = root
    height[root] = 0
    dfs(root, root)

    # ── Output ───────────────────────────────────────────────────────────────
    print("Graph:")
    for v in sorted_vertices:
        print(f"[{v}]: {', '.join(graph[v])}")

    print()
    print("Parent")
    for v in sorted_vertices:
        print(f"[{v}]: {parent.get(v, v)}")

    print()
    print("Height")
    for v in sorted_vertices:
        print(f"[{v}]: {height.get(v, 0)}")

    print()
    print("Articulation Points")
    for v in sorted_vertices:
        print(f"[{v}]: {v in ap_set}")

    print()
    print("Biconnected Components")
    for comp in bcc_list:
        print("{" + ", ".join(sorted(comp)) + "}")

main()