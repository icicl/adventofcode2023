import aoc
import networkx as nx
d = aoc.load(25)
edges = set()
nodes = set()
G = nx.Graph()
for i in d:
    a = i[:3]
    for b in i.split(' ')[1:]:
        G.add_edge(a,b)
G.remove_edges_from(nx.minimum_edge_cut(G))
part1 = aoc.pi([len(i) for i in nx.connected_components(G)])
part2 = 0