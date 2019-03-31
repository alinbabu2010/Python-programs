import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
pos={0:(0,.5),1:(.2,.8),2:(.2,.5),3:(.2,.2),4:(.4,.8),5:(.5,.5),6:(.4,.2),7:(.7,.85),8:(.8,.6),9:(.6,.3),10:(.9,.35)}
G.add_nodes_from(range(11))
G.add_edges_from([(0,1),(0,2),(0,3),(1,5),(1,6),(2,5),(3,4),(5,10),(4,7),(4,8),(6,9),(7,8),(8,9),(8,10)])
nx.draw(G,pos,with_labels=True)
plt.savefig("mygraph.pdf")
nx.write_edgelist(G,"mygraphedge.txt")
if nx.is_eulerian(G) :
    print("Graph is a euler graph")
else :
    print("Graph is not a euler graph")
plt.show()
