import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
from networkx.algorithms.bipartite.basic import color
from networkx.algorithms.matching import max_weight_matching

dp = {"core": ["a", "b", "c", "d", "e"]}

equivalencies = {"a": {"x": 2}, "b": {"z": 3}, "c": {"y": 2}, "d": {"z": 4}}

top_nodes = dp["core"]
bot_nodes = ["x", "y", "z"]

g = nx.Graph()

for n in top_nodes:
    g.add_node(n, bipartite='top')

for n in bot_nodes:
    g.add_node(n, bipartite='bottom')
    
for k, v in equivalencies.items():
    for kk, vv in v.items():
        g.add_edge(k, kk, weight=vv)

# print('is_bipartite:', nx.is_bipartite(g))
# nx.draw(g)
# plt.show()
p = {"a": (0, 10), "b": (0, 8), "c": (0, 6), "d": (0, 4), "e": (0, 2),
     "x": (10, 10), "y": (10, 8), "z": (10, 6)}

labels = [2 * w for e, w in nx.get_edge_attributes(g, 'weight').items()]
nx.draw_networkx(g, pos=p, with_labels=True, width=labels)

matching = max_weight_matching(g)

labels2 = [2 * w for e, w in nx.get_edge_attributes(g, 'weight').items() if e in matching]

nx.draw_networkx_edges(g, pos=p, edgelist=matching, width=labels2, edge_color='red')
plt.show()
