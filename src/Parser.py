# Import Library
import math

# Import kodingan sendiri
from Graph import Node, Graph
from Haversine import haversine_distance

# =======================================Class Definition================================================
"""
    class Parser adalah class yang digunakan untuk mengekstrak input dari file external
    menjadi graf
"""
class Parser:
    def __init__(self):
        # Constructor 
        # Mengisi attribute kelas astar dengan atribute default atau atribute masukan
        self.graph = Graph()
        self.bool_adj = []
        self.list_of_node =[]
        self.num_of_node = 0

    def read_from_file(self,filename):
        inputs = open('test/'+ filename +'.txt','r').read().split('\n')

        # Dapatkan num_of_node pada input txt 
        self.num_of_node = int(inputs[0])

        # Dapatkan informasi node pada input txt 
        for i in range(1, 1+self.num_of_node):
            input = inputs[i].split(' ')
            self.list_of_node.append(Node(name=input[0], index=i-1, latitude=float(input[1]),longitude=float(input[2])))
        
        # Dapatkan adjacency matrix dalam bentuk boolean pada input txt
        for i in range(self.num_of_node+1, 2*self.num_of_node+1):
            bool_adj_row = []
            input = inputs[i].split(' ')
            for is_adj in input:
                bool_adj_row.append(int(is_adj))
            self.bool_adj.append(bool_adj_row)
        
        # Buat graf permulaan dan isi adjacency matrixnya satu per satu berdasarkan adjacency matrix boolean
        self.graph = Graph(size=self.num_of_node,list_of_node=self.list_of_node)
        for i in range(self.num_of_node):
            for j in range(self.num_of_node):
                if (self.bool_adj[i][j] == 1 and self.graph.adj[i][j] == math.inf):
                    self.graph.add_edge(i,j,haversine_distance(self.list_of_node[i],self.list_of_node[j]))
            
    def display_attr(self,bool_adj=False,node=False, graph_adj=False):
        # Menampilkan data dari file txt dan menampilkan adjacency matriks pada graf
        if bool_adj:
            i = 0
            print("Boolean Adjacency matrix")
            print("     ",end="")
            for node in self.list_of_node:
                print(node.name,end=(5-len(node.name))*" ")
            print()
            for row in self.bool_adj:
                print(self.list_of_node[i].name,end=(5-len(self.list_of_node[i].name))*" ")
                for col in row:
                    print(col,end=(5-len(str(col)))*" ")
                print()
                i = i +1
        if graph_adj:
            print()
            print("Graph weighted adjacency matrix")
            self.graph.display_adj()
        if node:
            print()
            print("List of node")
            for node in self.list_of_node:
                print(node)
# =====================================================================================================
        
