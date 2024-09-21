from collections import defaultdict, deque

# Exercise 1: Depth-First Search (DFS)
# Given a graph represented by an adjacency list, perform DFS starting from a given node.
def dfs(node, graph, visited):
    # TODO: Fill in the logic
    pass

# Exercise 2: Breadth-First Search (BFS)
# Given a graph represented by an adjacency list, perform BFS starting from a given node.
def bfs(start, graph):
    # TODO: Fill in the logic
    pass

# Exercise 3: Check if a Graph is Connected
# Given a graph, check whether it is connected.
def is_connected(graph):
    # TODO: Fill in the logic
    return False

# Exercise 4: Find the Shortest Path from Source to Target (BFS)
# Given a graph and two nodes, find the shortest path from source to target using BFS.
def shortest_path_bfs(source, target, graph):
    # TODO: Fill in the logic
    return []

# Exercise 5: Detect Cycle in an Undirected Graph
# Detect if there is a cycle in an undirected graph.
def detect_cycle_undirected(graph):
    # TODO: Fill in the logic
    return False

# Exercise 6: Detect Cycle in a Directed Graph
# Detect if there is a cycle in a directed graph.
def detect_cycle_directed(graph):
    # TODO: Fill in the logic
    return False

# Exercise 7: Count Connected Components in a Graph
# Count and return the number of connected components in the graph.
def count_connected_components(graph):
    # TODO: Fill in the logic
    return 0

# Exercise 8: Topological Sort (for Directed Acyclic Graph)
# Perform topological sort on a directed acyclic graph.
def topological_sort(graph):
    # TODO: Fill in the logic
    return []

# Exercise 9: Find All Paths between Two Nodes
# Find all paths between two nodes in the graph.
def find_all_paths(source, target, graph):
    # TODO: Fill in the logic
    return []

# Utility function to add an edge to the graph
def add_edge(graph, u, v, directed=False):
    graph[u].append(v)
    if not directed:
        graph[v].append(u)

# Sample graph creation
def create_sample_graph():
    graph = defaultdict(list)
    add_edge(graph, 1, 2)
    add_edge(graph, 1, 3)
    add_edge(graph, 2, 4)
    add_edge(graph, 3, 4)
    add_edge(graph, 4, 5)
    return graph

# Sample directed graph creation
def create_sample_directed_graph():
    graph = defaultdict(list)
    add_edge(graph, 1, 2, directed=True)
    add_edge(graph, 2, 3, directed=True)
    add_edge(graph, 3, 4, directed=True)
    return graph

# Test cases for each exercise using assertions
def run_tests():
    # Sample undirected graph
    sample_graph = create_sample_graph()

    # Sample directed graph
    directed_graph = create_sample_directed_graph()

    # Test DFS
    print("Exercise 1: DFS")
    try:
        visited = set()
        dfs(1, sample_graph, visited)
        # Expected output: traversal of the graph in DFS order
    except AssertionError:
        print("DFS failed!")

    # Test BFS
    print("Exercise 2: BFS")
    try:
        bfs(1, sample_graph)
        # Expected output: traversal of the graph in BFS order
    except AssertionError:
        print("BFS failed!")

    # Test isConnected
    print("Exercise 3: Is Connected")
    result_connected = is_connected(sample_graph)
    assert result_connected, "Expected true but got false"

    # Test shortestPathBFS
    print("Exercise 4: Shortest Path BFS")
    shortest_path = shortest_path_bfs(1, 5, sample_graph)
    assert shortest_path == [1, 3, 4, 5], f"Expected [1, 3, 4, 5] but got {shortest_path}"

    # Test detectCycleUndirected
    print("Exercise 5: Detect Cycle in Undirected Graph")
    has_cycle_undirected = detect_cycle_undirected(sample_graph)
    assert has_cycle_undirected, "Expected true but got false"

    # Test detectCycleDirected
    print("Exercise 6: Detect Cycle in Directed Graph")
    has_cycle_directed = detect_cycle_directed(directed_graph)
    assert not has_cycle_directed, "Expected false but got true"

    # Test countConnectedComponents
    print("Exercise 7: Count Connected Components")
    connected_components = count_connected_components(sample_graph)
    assert connected_components == 1, f"Expected 1 but got {connected_components}"

    # Test topologicalSort
    print("Exercise 8: Topological Sort")
    topo_sort = topological_sort(directed_graph)
    assert topo_sort == [1, 2, 3, 4], f"Expected [1, 2, 3, 4] but got {topo_sort}"

    # Test findAllPaths
    print("Exercise 9: Find All Paths")
    all_paths = find_all_paths(1, 5, sample_graph)
    assert len(all_paths) == 2, f"Expected 2 paths but got {len(all_paths)}"

    print("All tests completed.")

# Run tests
run_tests()