

try:
    import queue
except ImportError:
    import Queue as queue

from queue import PriorityQueue

graph = {
    'Sports Complex': {'Siwaka': 450},
    'Siwaka': {'Phase.1A': 10, 'Phase.1B': 230, 'Sports Complex': 450},
    'Phase.1A': {'Phase.1B': 100, 'Madaraka': 850, 'Siwaka': 10},
    'Phase.1B': {'Phase2': 112, 'STC': 50, 'Siwaka': 230},
    'STC': {'Parking lot': 250, 'Phase.1B': 50},
    'Phase2': {'J1': 600, 'Phase3': 500, 'Phase.1B': 112},
    'J1': {'Madaraka': 200, 'Phase2': 600},
    'Madaaraka': {'Parking lot': 700, 'J1': 200, 'Ph1.A': 850},
    'Phase3': {'Parking lot': 350, 'Phase2': 500},
    'Parking lot': {'Phase3': 350, 'STC': 250, 'Madaraka': 700},

}

heuristic = {'Sports Complex': 730, 'Siwaka': 405, 'Phase.1A': 380, 'Phase.1B': 280, 'STC': 213, 'Phase2': 210, 'J1': 500,
             'Phase3': 160, 'Madaraka': 630, 'Parking lot': 0}


def Greedy(graph, start, goal):
    visited = set()
    expanded = []
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        current = node
        print(" current : {}".format(current))
        if current not in visited:
            visited.add(current)
            expanded.append(current)

            if current == goal:
                return node, expanded

            neighbours = graph[current]
            print(neighbours)
            for i in neighbours:
                if i not in visited:
                    total_cost = heuristic[i]
                    queue.put((total_cost, i))


path, expanded = Greedy(graph, 'Sports Complex', 'Parking lot')
output = [char for char in path]
print("\nThe optimal path using a greedy search is : " + "->".join(output))
print("The states expanded are:")
print(expanded)


def UCS(graph, start, goal):
    visited = set()
    expanded = []
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        current = node
        if current not in visited:
            visited.add(current)
            expanded.append(current)

            if current == goal:
                return node, expanded

            neighbours = graph[current]
            for i in neighbours:
                if i not in visited:
                    total_cost = cost + neighbours[i]
                    queue.put((total_cost, i))


pathUCS, expandedUCS = UCS(graph, 'Sports Complex', 'Parking lot')
outputUCS = [char for char in path]
print("\nThe optimal path using a greedy search is : " + "->".join(output))
print("The states expanded are:")
print(expandedUCS)

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes = ["Sports Complex", "Siwaka"]
G.add_nodes_from(nodes)
G.nodes()  # confirm nodes
# Add Edges and their weights
G.add_edge("Sports Complex", "Siwaka", weight="450")
G.add_edge("Siwaka", "Phase.1A", weight="10")
G.add_edge("Siwaka", "Phase.1B", weight="10")
G.add_edge("Phase.1A", "Phase.1B", weight="100")
G.add_edge("Phase.1B", "STC", weight="100")
G.add_edge("Phase.1B", "Phase2", weight="112")
G.add_edge("Phase2", "J1", weight="600")
G.add_edge("J1", "Madaraka", weight="200")
G.add_edge("Phase2", "Phase3", weight="500")
G.add_edge("Phase3", "Parking lot", weight="350")
G.add_edge("STC", "Parking lot", weight="250")
G.add_edge("Phase2", "STC", weight="50")

# position the nodes to resemble the map for Nairobi
G.nodes["Sports Complex"]['pos'] = (1, 7)
G.nodes["Siwaka"]['pos'] = (3, 7)
G.nodes["Phase.1A"]['pos'] = (5, 7)
G.nodes["Phase.1B"]['pos'] = (5, 5)
G.nodes["STC"]['pos'] = (5, 3)
G.nodes["Phase2"]['pos'] = (7, 5)
G.nodes["J1"]['pos'] = (9, 5)
G.nodes["Madaraka"]['pos'] = (11, 5)
G.nodes["Phase3"]['pos'] = (7, 3)
G.nodes["Parking lot"]['pos'] = (7, 1)

# store all positions in a variable
node_pos = nx.get_node_attributes(G, 'pos')
# call BFS to return set of all possible routes to the goal

print("route_list : {}".format(expanded))
route_list = expanded
# color the nodes in the route_bfs
node_col = ['green' if not node in route_list else 'blue' for node in G.nodes()]
blue_colored_edges = list(zip(route_list, route_list[1:]))
# color the edges as well
# print(blue_colored_edges)
edge_col = ['green' if not edge in blue_colored_edges else 'blue' for edge in G.edges()]
arc_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col)
# nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)


nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()

print("route_list for UCS : {}".format(expanded))
route_list = expandedUCS
# color the nodes in the route_bfs
node_col = ['yellow' if not node in route_list else 'purple' for node in G.nodes()]
blue_colored_edges = list(zip(route_list, route_list[1:]))
# color the edges as well
# print(blue_colored_edges)
edge_col = ['yellow' if not edge in blue_colored_edges else 'purple' for edge in G.edges()]
arc_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col)
# nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)


nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
