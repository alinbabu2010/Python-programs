import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
n=input("Enter the number of vertex pair\n");
print("Enter the vertex pair of graph");
for i in range(n):
    a,b=raw_input().split();
    G.add_edge(a,b)
nx.draw(G,with_labels=True)
if nx.is_connected(G) :
    print("Graph is a connected graph")
else :
    print("Graph is not a connected graph")
if nx.is_tree(G) :
    print("Graph is a tree")
else :
    print("Graph is not a tree");
plt.show()
