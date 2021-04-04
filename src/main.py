from Graph import Graph
from Astar import astar_find
from Parser import Parser

#  Membaca input dari file txt dan menulisnya ke layar
import os
os.chdir("..") # Pindah ke directory atas
filename = input("Masukkan nama file (tanpa ekstensi): ")
filecontent = Parser()
filecontent.read_from_file(filename)
filecontent.display_attr(node=True,bool_adj=True,graph_adj=True)

graph = filecontent.graph

start_node_name = input("Masukkan nama node awal: ")
end_node_name = input("Masukkan nama node tujuan: ")
start_node = graph.find_node(name=start_node_name)
end_node = graph.find_node(name=end_node_name)
# print(start_node)
# print(end_node)

path = astar_find(graph,start_node,end_node)[0]
price = astar_find(graph,start_node,end_node)[1]
print(graph.transform_path(path))
print(price)