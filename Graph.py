class Graph:
    def __init__(self, nodes, graph_dict):
        self.nodes = nodes
        self.graph_dict = graph_dict

    def bfs(self, start, goal):
        visited = []
        buffer = []
        trace = dict()
        buffer.append(start)
        while len(buffer) != 0:
            n = buffer.pop(0)
            if n not in visited:
                if n == goal:
                    print("\nBFS solution:")
                    break
                visited.append(n)
                for neighbour in graph_dict[n]:
                    if neighbour not in buffer and neighbour not in visited:
                        buffer.append(neighbour)
                        trace[neighbour] = n

        route = " " + goal

        def path(trace, route, prev_curr_node):
            route += ">-" + prev_curr_node
            if prev_curr_node == start:
                return route
            else:
                return path(trace, route, trace[prev_curr_node])

        solution = path(trace, route, trace[goal])
        print(solution[::-1])

    def backtrack(self, new_node, dfs_stack):
        n = dfs_stack.pop()

        # remove the node (key and value) from graph_dict
        del graph_dict[n]

        # remove the dead-end value from the previous node
        del graph_dict[dfs_stack[-1]][0]

        # update node to previous node
        new_node = dfs_stack[-1]

        return new_node

    def dfs(self, node, goal, dfs_stack):
        if node == goal:
            dfs_stack.append(node)
            return dfs_stack
        else:
            dfs_stack.append(node)
            while True:
                if graph_dict[node][0] in dfs_stack or dfs_stack[-1] > graph_dict[node][0]:
                    if len(graph_dict[node]) == 1:
                        node = self.backtrack(graph_dict[node][0], dfs_stack)
                        break
                    else:
                        del graph_dict[node][0]
                else:
                    break
            return self.dfs(graph_dict[node][0], goal, dfs_stack)


# driver code
if __name__ == '__main__':
    n = list(map(str, input("Enter all the nodes: ").strip().split()))
    graph_dict = {}
    for node in n:
        print(f"Enter the adjoining nodes of {node}: ", end='')
        graph_dict[node] = list(map(str, input().strip().split()))
    gr = Graph(n, graph_dict)
    start = input("Enter start node: ").strip()
    goal = input("Enter your goal node: ").strip()
    gr.bfs(start, goal)
    dfs_stack = [start]
    dfs_soln = gr.dfs(graph_dict[start][0], goal, dfs_stack)
    print("\nDFS solution:")
    for i in dfs_soln:
        if i == goal:
            print(i)
            break
        print(f"{i}->", end="")