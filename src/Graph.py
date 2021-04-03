# Import Modul
import math
class Node:
    def __init__(self,name="",index=0,longitude=0,latitude=0):
        self.index = index
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return (str(self.index)+" "+self.name+" "+str(self.longitude)+ " "+str(self.latitude))

# Representasi Graf dengan matriks ketetanggaan berbobot
class Graph():
    def __init__(self, size=0,adj=[], list_of_node = []):
        self.size = size
        self.list_of_node = []
        for node in list_of_node:
            self.list_of_node.append(node)
        self.adj = []
        if (adj==[]):
            for i in range(size):
                self.adj.append([math.inf for i in range(size)])
        else:
            for row in adj:
                adj_row = []
                for col in row:
                    adj_row.append(col)
                self.adj.append(adj_row)

    def find_node(self,index=None,name=None):
        try:
            if(index!= None ):
                return [node for node in self.list_of_node if node.index==index][0]
            if(name!= None ):
                return[node for node in self.list_of_node if node.name==name][0]
        except:
            print("invalid index or name")
        
    def add_edge(self, orig, dest, length = 0):
        try:
            if (orig == dest): raise IndexError
            self.adj[orig][dest] = length
            self.adj[dest][orig] = length
        except IndexError:
            print("Invalid index")

    def remove_edge(self, orig, dest):
        try:
            if (orig == dest): raise IndexError
            self.adj[orig][dest] = math.inf
            self.adj[dest][orig] = math.inf
        except IndexError:
            print("Invalid index")
        
    def display_adj(self):
        for row in self.adj:
            for val in row:
                print(val,end=(8-len(str(val)))*" ")
            print()
    
    def transform_path(self,path):
        new_path =""
        path= path.split('-')
        for node in path:
            new_path = new_path+ self.find_node(index=int(node)).name +"-"
        return new_path[:len(new_path)-1]