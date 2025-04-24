import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def random_node(g):  # Санамсаргүй узел сонгох
    return [np.random.choice(list(g.nodes()))]

def dismantle(g, function, **args):  # Узелүүдийг аажмаар устгаж, их бүрэлдэхүүн хэсгийн хэмжээг хэмжих
    g = g.copy()
    total_nodes = g.number_of_nodes()
    removed_nodes = []
    components = []

    while g.number_of_nodes() > 1:
        n = function(g, **args)[0]
        g.remove_node(n)
        removed_nodes.append((len(removed_nodes)+1)/total_nodes)
        comps = list(nx.connected_components(g))
        g_size = max([len(c) for c in comps]) / total_nodes if comps else 0
        components.append(g_size)
    
    return removed_nodes, components

def get_sorted_nodes(g, score, reverse=True):  # Узелүүдийг оноогоор нь эрэмбэлэх
    nodes = score(g)
    if isinstance(nodes, dict):
        nodes = list(nodes.items())
    sorted_nodes = sorted(nodes, key=lambda x: x[1], reverse=reverse)
    return [x[0] for x in sorted_nodes]

def plot_dismantle(x, y):  # График дүрслэл
    plt.plot(x, y, marker='o')
    plt.xlabel("Устгасан узелүүдийн хувь")
    plt.ylabel("Их бүрэлдэхүүн хэсгийн хэмжээ")
    plt.title("Сүлжээний эмзэг байдлын шинжилгээ")
    plt.grid(True)
    plt.show()
