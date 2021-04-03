# Import Modul
import math
from Haversine import haversine_distance

"""
    class Astar_Node merepresentasikan node pada state space tree yang dibentuk saat algoritma 
    pencarian astar dilakukan. Astar_Node nantinya akan dimasukkan ke dalam antrian dimana Astar_Node 
    dengan total harga terendah dan belum dikunjungi akan dikunjungi terlebih dahulu. Astar_Node yang 
    sudah dikunjungi akan disimpan ke dalam list.
"""
class Astar_Node:
    """
        path adalah node yang dilalui untuk mencapai node saat ini
        g adalah harga dari node start hingga node saat ini dengan path tertentu
        h adalah estimasi harga dari node saat ini ke node tujuan secara heuristik
        f adalah total harga dari node saat ini (f = g + h)
    """
    def __init__(self, path=None, index=None, g=0, h=0, f=0):
        self.path = path
        self.index = index

        self.g = g
        self.h = h
        self.f = f

    def __eq__(self, other):
        return self.index == other.index
    
    def __str__(self):
        return(self.path+ " f: "+ str(self.f) +" g: "+ str(self.g)+" h: "+str(self.h))

def astar_find(graph,start,end):
    start_astar_node = Astar_Node(path=str(start.index)+"-",index=start.index)
    end_astar_node = Astar_Node(path="",index=end.index)
    
    to_visit = []
    has_visited =[]

    to_visit.append(start_astar_node)
    
    while (len(to_visit) > 0):
        
        to_visit.sort(key= lambda x:x.f)
        curr_astar_node = to_visit[0]

        # Debug
        # curr_astar_node = [astar_node for astar_node in to_visit if astar_node.f == min(to_visit, key= lambda x:x.f).f][0]
        # for node in to_visit:
        #     print (node, end=" | ")
        # print()
        # to_visit.pop(to_visit.index(curr_astar_node))

        to_visit.pop(0)
        has_visited.append(curr_astar_node)

        if (curr_astar_node==end_astar_node):
            return curr_astar_node.path[:len(curr_astar_node.path)-1]
        astar_candidate = []
        
        for i in range(graph.size):
            if(graph.adj[curr_astar_node.index][i] != math.inf):
                # heurisitic_price = matrix_heuristic_price[i][end_astar_node.index]
                heurisitic_price = haversine_distance(graph.find_node(index=i),graph.find_node(index=end_astar_node.index))
                path_price = curr_astar_node.g + graph.adj[curr_astar_node.index][i]
                new_astar_node = Astar_Node(path=curr_astar_node.path+str(i)+"-", index=i, g=path_price , h=heurisitic_price, f=heurisitic_price+path_price)
                astar_candidate.append(new_astar_node)
        
        for astar_node in astar_candidate:
            if(len([visited_astar_node for visited_astar_node in has_visited if visited_astar_node == astar_node])>0):
                continue
            if (len([astar_node_2 for astar_node_2  in to_visit if astar_node == astar_node_2  and astar_node.f > astar_node_2.f])) > 0:
                continue
            to_visit.append(astar_node)
    return None