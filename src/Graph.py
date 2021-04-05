# Import Library
import math

# =======================================Class Definition================================================
"""
    Class Node merepresentasikan persimpangan pada suatu jalan. Node disini berbeda dengan Astar_Node
    dimana Astar_Node adalah node yang digunakan untuk membantu pencarian dengan algoritma astar. Node disini
    murni representasi dari suatu simpangan
"""
class Node:
    """
        index adalah index node pada adjacency matriks di graf
        name adalah nama persimpangan
        longitude adalah garis bujur(dalam derajat) dari persimpangan
        latitude adalah garis lintang(dalam derajat) dari persimpangan
    """
    def __init__(self,name="",index=0,longitude=0,latitude=0):
        # Constructor 
        # Mengisi attribute kelas Node dengan atribute default atau atribute masukan
        self.index = index
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        # Function overloading str()
        # Mengubah representasi Node saat di print
        return (str(self.index)+" "+self.name+" "+str(self.longitude)+ " "+str(self.latitude))

"""
    Class Graph merupakan representasi Graf dengan sisi yaitu jalan antar persimpangan 
    Graf dirrepresentasikan dengan matriks ketetanggaan berbobot. Graf akan diload dari file 
    external dan jarak antar node yang bertetangga akan dihitung dengan haversian_distance
"""

class Graph():
    """
        size adalah banyaknya node sekaligus menjadi ukuran matriks ketetanggaan (size*size)
        list_of_node merupakan list yang berisikan informasi umum dari node yang ada di graf
        adj merupakan matriks ketetanggaan dari graf
    """
    def __init__(self, size=0,adj=[], list_of_node = []):
        # Constructor 
        # Mengisi attribute kelas Graph dengan atribute default atau atribute masukan

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
        # Menemukan node dengan parameter index atau nama
        try:
            if(index!= None ):
                return [node for node in self.list_of_node if node.index==index][0]
            if(name!= None ):
                return[node for node in self.list_of_node if node.name==name][0]
        except:
            print("invalid index or name")
        
    def add_edge(self, orig, dest, length = 0):
        # Menambahkan sisi antar node dengan memodifikasi matriks ketetanggaan
        try:
            if (orig == dest): raise IndexError
            self.adj[orig][dest] = length
            self.adj[dest][orig] = length
        except IndexError:
            print("Invalid index")

    def remove_edge(self, orig, dest):
        # Menghilangkan sisi antar node dengan memodifikasi matriks ketetanggaan
        try:
            if (orig == dest): raise IndexError
            self.adj[orig][dest] = math.inf
            self.adj[dest][orig] = math.inf
        except IndexError:
            print("Invalid index")
        
    def display_adj(self):
        # Menampilkan matriks ketetanggaan
        i = 0
        print("     ",end="")
        for node in self.list_of_node:
            print(node.name,end=(5-len(node.name))*" ")
        print()
        for row in self.adj:
            print(self.list_of_node[i].name,end=(5-len(self.list_of_node[i].name))*" ")
            for val in row:
                print(val,end=(5-len(str(val)))*" ")
            print()
            i = i +1
    
    def transform_path(self,path):
        # Merubah path dari index dengan nama
        new_path =""
        path= path.split('-')
        for node in path:
            new_path = new_path+ self.find_node(index=int(node)).name +"-"
        return new_path[:len(new_path)-1]
# =====================================================================================================