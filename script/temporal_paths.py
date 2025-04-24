import networkx as nx

def create_temporal_graph(edges):
    G = nx.DiGraph()
    for u, v, t_start, t_end in edges:
        G.add_edge(u, v, time=t_start, end_time=t_end)
    return G

def shortest_path(graph, source, target):
    return nx.shortest_path(graph, source=source, target=target)

def fastest_path(graph, source, target):
    return nx.shortest_path(graph, source=source, target=target, weight='end_time')

def foremost_path(graph, source, target):
    return nx.shortest_path(graph, source=source, target=target, weight='time')

def fastest_shortest_path(graph, source, target):
    all_shortest_paths = list(nx.shortest_simple_paths(graph, source=source, target=target))
    return min(all_shortest_paths, key=lambda p: sum(graph[u][v]['end_time'] for u, v in zip(p[:-1], p[1:])))

def shortest_fastest_path(graph, source, target):
    all_fastest_paths = list(nx.shortest_simple_paths(graph, source=source, target=target))
    return min(all_fastest_paths, key=lambda p: len(p))
