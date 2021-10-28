import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","STC",
           "Phase2","J1","Mada","Phase3","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("STC","Ph.1B",weight="50")
G.add_edge("STC","Phase2",weight="50")
G.add_edge("Ph.1B","Ph.1A",weight="100")
G.add_edge("Ph.1B","Siwaka",weight="230")
G.add_edge("Ph.1B","Phase2",weight="112")
G.add_edge("SportsComplex","Siwaka",weight="450")
G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("Phase3","ParkingLot",weight="350")
G.add_edge("STC","ParkingLot",weight="250")
G.add_edge("Mada","ParkingLot",weight="700")
#position the nodes to resemble Nairobis map
G.nodes["STC"]['pos']=(0,0)
G.nodes["Ph.1B"]['pos']=(0,2)
G.nodes["Ph.1A"]['pos']=(0,4)
G.nodes["Siwaka"]['pos']=(-2,4)
G.nodes["SportsComplex"]['pos']=(-4,4)
G.nodes["Phase2"]['pos']=(2,2)
G.nodes["J1"]['pos']=(4,2)
G.nodes["Mada"]['pos']=(6,2)
G.nodes["Phase3"]['pos']=(4,0)
G.nodes["ParkingLot"]['pos']=(4,-2)
#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')

arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= 'blue', node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= 'yellow')
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()



# QN 2. Greedy BFS
G.nodes["STC"]

from collections import defaultdict 
class BfsTraverser: 
  # Constructor 
  def __init__(self): 
    self.visited = []
    self.end_search = False
  def BFS(self,graph, start_node, goal_node):
    queue = []
    queue.append(start_node)
    #print(queue)
    #set of visited nodes
    self.visited.append(start_node)
    while queue and not self.end_search: 
      # Dequeue a vertex from 
      s = queue.pop(0)          

      # Get all adjacent vertices of the 
      # dequeued vertex s. If a adjacent 
      # has not been visited, then mark it 
      # visited and enqueue it 
      for i in list(graph[s]):
        if i not in self.visited:
          #print ("Command; Drive from ",s," to " ,i, " Estate/Junction", end = "\n") 
          #print("Current Node is",i, " but the goal Node is ",goal_node)
          print ("Command; Drive to " ,i, " Estate/Junction", end = "\n")
          if i is goal_node:
            print("We have reached ",i," the final destination")
            self.visited.append(i)
            self.end_search = True
            break
          else:
            #print("Here",self.end_search)
            queue.append(i)
            #visited[i] = True
            self.visited.append(i)


