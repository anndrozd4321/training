#import numpy as np
#import numpy.random as rand
import networkx as nx
from matplotlib import pyplot as plt
#import graphviz as gr

G = nx.DiGraph()
countNodes = int(input("Введите количество работ: "))

for i in range(countNodes*2):
    G.add_node(i)
i = 0
number = 1
while i != countNodes*2:
    G.add_edge(i, i+1, weight=number)
    number = number + 1
    i = i + 2

for i in nx.get_edge_attributes(G, 'weight'):
    print(i)

edge_weight = nx.get_edge_attributes(G, 'weight')

for i in edge_weight:
    print(i)
    print(edge_weight)

print(list(G.nodes))
print(list(G.edges))

#for i in range(countNodes):
#    preEdges = int(input("Введите работы которым предшествует работа ", countNodes))


pos = nx.spring_layout(G)
plt.figure()
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, edge_color='black', width=1, linewidths=1, node_size=150, node_color='black', alpha=0.9) #labels={node:node for node in G.nodes()}
nx.draw_networkx_edge_labels(G, pos, font_color='black', edge_labels=labels, font_size=10)
plt.axis('off')
plt.show()
