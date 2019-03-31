import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
pos={0:(0,.5),1:(.2,.8),2:(.2,.5),3:(.2,.2),4:(.4,.8),5:(.4,.5),6:(.4,.2),7:(.8,.8),8:(.9,.5),9:(.8,.2),10:(1.0,.3)}
G.add_nodes_from(range(11))
G.add_edges_from([(0,1),(0,2),(0,3),(1,5),(1,6),(2,5),(3,4),(5,10),(4,7),(4,8),(6,9),(7,8),(8,9),(8,10)])
nx.draw_networkx(G,pos,with_labels=True)
nx.write_edgelist(G,"mygraphedge.txt")
if nx.is_connected(G) :
    print("Graph is a connected graph")
else :
    print("Graph is not a connected graph")
    
plt.show()
