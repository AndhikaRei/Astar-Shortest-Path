# Import library
import math

# Import kodingan sendiri
from Haversine import haversine_distance

# =======================================Class Definition================================================
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
        # Constructor 
        # Mengisi attribute kelas astar dengan atribute default atau atribute masukan

        self.path = path
        self.index = index

        self.g = g
        self.h = h
        self.f = f

    def __eq__(self, other):
        # Operator overloading ==
        # Dua buah Astar_Node dikatakan sama apabila indexnya sama
        return self.index == other.index
    
    def __str__(self):
        # Function overloading str()
        # Mengubah representasi Astar_Node saat di print
        return(self.path+ " f: "+ str(self.f) +" g: "+ str(self.g)+" h: "+str(self.h))

# Algoritma pencarian dengan astar
def astar_find(graph,start,end):
    # I.S graph adalah graf yang valid, start dan end adalah node yang valid
    # F.S Mengirimkan path dengan jalur terpendek dari node start ke node end

    # Inisialisasi Astar_Node dari node start dan node goal
    start_astar_node = Astar_Node(path=str(start.index)+"-",index=start.index)
    end_astar_node = Astar_Node(path="",index=end.index)
    
    # Deklarasi list node yang sudah dikunjungi dan akan dikunjungi
    to_visit = []
    has_visited =[]

    # Astar_Node pertama adalah Astar_Node start
    to_visit.append(start_astar_node)
    
    # Selama masih ada Astar_Node yang bisa dikunjungi lakukan algorima pencarian astar
    while (len(to_visit) > 0):
        
        # Astar_Node yang akan dikunjungi diurutkan berdasarkan nilai f nya 
        to_visit.sort(key= lambda x:x.f)
        
        # Ambil Astar_Node dengan nilai f terkecil dan kunjungi Astar_Node tersebut, simpan sebagai curr_astar_node
        curr_astar_node = to_visit[0]
        to_visit.pop(0)
        has_visited.append(curr_astar_node)

        # Jika curr_astar_node yang sekarang merupakan node tujuan maka return pathnya
        if (curr_astar_node==end_astar_node):
            return [curr_astar_node.path[:len(curr_astar_node.path)-1], curr_astar_node.g]

        # Inisialisasi calon Astar_Node yang akan dikunjungi
        astar_candidate = []
        
        """
            1) Untuk semua tetangga dari curr_astar_node yang ada jadikan dia calon Astar_Node yang akan dikunjungi
            2) Untuk semua tetangga dari curr_astar_node
                1> path nya adalah path dari curr_astar_node ditambah index nya
                2> h nya adalah haversian_distance nya terhadap node goal
                3> g nya harga dari curr_astar_node sekarang ditambah harga menuju tetangga
                4> f nya adalah h + g
        """
        for i in range(graph.size):
            if(graph.adj[curr_astar_node.index][i] != math.inf):
                heurisitic_price = haversine_distance(graph.find_node(index=i),graph.find_node(index=end_astar_node.index))
                path_price = curr_astar_node.g + graph.adj[curr_astar_node.index][i]
                new_astar_node = Astar_Node(path=curr_astar_node.path+str(i)+"-", index=i, g=path_price , h=heurisitic_price, f=heurisitic_price+path_price)
                astar_candidate.append(new_astar_node)
        
        # Evaluasi apakah calon Astar_Node layak untuk dikunjungi
        for astar_node in astar_candidate:

            # Jika ditemukan Astar_Node yang sama (==) di list sudah dikunjungi maka jangan kunjungi Astar_Node kandidat
            if(len([visited_astar_node for visited_astar_node in has_visited if visited_astar_node == astar_node])>0):
                continue

            # Jika ditemukan Astar_Node yang sama (==) dan berada di list akan dikunjungi dan Astar_Node yang sekarang 
            # F nya lebih mahal (Astar_Node yang sekarang bukan best solution so far) maka jangan kunjungi Astar_Node kandidat
            if (len([astar_node_2 for astar_node_2  in to_visit if astar_node == astar_node_2  and astar_node.f > astar_node_2.f])) > 0:
                continue

            # Astar_Node sekarang merupakan calon the best solution so far
            to_visit.append(astar_node)
            
    # Tidak ditemukan path
    return [None,"infinity"]

# =======================================================================================================