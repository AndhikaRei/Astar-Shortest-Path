#  Main Program tanpa visualisasi untuk mengecek jalur terpendek
from Graph import Graph
from Astar import astar_find
from Parser import Parser

import os
os.chdir("..") # Pindah ke directory atas

#  Membaca input dari file txt dan menjadikannya dalam bentuk graf
filename = input("Masukkan nama file (tanpa ekstensi): ")
filecontent = Parser()
filecontent.read_from_file(filename)

#  Menuliskan data yang ada pada file txt dan graf yang dibentuk dari file txt 
filecontent.display_attr(node=True,bool_adj=True,graph_adj=True)

# Meload graf dari file txt
graph = filecontent.graph

# Masukkan nama simpul awal dan simpul tujuan
start_node_name = input("Masukkan nama node awal: ")
end_node_name = input("Masukkan nama node tujuan: ")

# Cari simpul dengan nama tersebut di dalam graf
start_node = graph.find_node(name=start_node_name)
end_node = graph.find_node(name=end_node_name)

# Melakukan pencarian dengan algoritma astar
path = astar_find(graph,start_node,end_node)[0]
price = astar_find(graph,start_node,end_node)[1]

# Menuliskan jalur yang didapat
print(graph.transform_path(path))
print(price)