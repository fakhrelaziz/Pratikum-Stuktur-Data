class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None  
        self.right = None  

class BST:
    def __init__(self):
        self.root = None 

    #Fungsi untuk nambahin buku (Insert)
    def insert(self, id_buku, judul):
        if self.root is None:
            #Kalau tree masih kosong, jadikan buku pertama sebagai root
            self.root = Node(id_buku, judul)
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
        else:
            #Kalau udah ada isinya, kita panggil fungsi bantuan buat nyari posisi
            self._insert_rekursif(self.root, id_buku, judul)

    def _insert_rekursif(self, node, id_buku, judul):
        #Buku dengan ID yang lebih kecil dari root akan diletakkan di cabang kiri
        if id_buku < node.id_buku:
            if node.left is None:
                node.left = Node(id_buku, judul) 
                print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            else:
                self._insert_rekursif(node.left, id_buku, judul) 
        
        #ID yang lebih besar akan diletakkan di cabang kanan.
        elif id_buku > node.id_buku:
            if node.right is None:
                node.right = Node(id_buku, judul)
                print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            else:
                self._insert_rekursif(node.right, id_buku, judul)
        
    #Fungsi untuk nyari buku (Search)
    def search(self, id_buku):
        hasil = self._search_rekursif(self.root, id_buku)
        if hasil is not None:
            print(f"[SEARCH] Mencari ID {id_buku}... Ditemukan! Judul: {hasil.judul}")
        else:
            print(f"[SEARCH] Mencari ID {id_buku}... Data tidak ditemukan.")

    def _search_rekursif(self, node, id_buku):
        #Base case
        if node is None or node.id_buku == id_buku:
            return node
        
        #Kalau ID yang dicari lebih kecil, belok ke kiri
        if id_buku < node.id_buku:
            return self._search_rekursif(node.left, id_buku)
        
        #Kalau lebih besar, belok ke kanan
        return self._search_rekursif(node.right, id_buku)

    #Traversal In-Order (Kiri -> Root -> Kanan)
    def traversal_inorder(self):
        self.nomor_urut = 1 #Bikin variabel sementara buat print angka 1, 2, 3
        self._inorder_rekursif(self.root)

    def _inorder_rekursif(self, node):
        if node is not None:
            self._inorder_rekursif(node.left)
            print(f"{self.nomor_urut}. {node.id_buku} - {node.judul}")
            self.nomor_urut += 1 #Tambah 1 tiap habis nge-print
            self._inorder_rekursif(node.right)

    #Cari nilai paling kecil (Mentok ke Kiri)
    def get_min(self):
        if self.root is None:
            return None
        node_sekarang = self.root
        #Looping terus selama sebelah kiri masih ada
        while node_sekarang.left is not None:
            node_sekarang = node_sekarang.left
        return node_sekarang.id_buku

    #Cari nilai paling besar (Mentok ke Kanan)
    def get_max(self):
        if self.root is None:
            return None
        node_sekarang = self.root
        #Looping terus selama sebelah kanan masih ada
        while node_sekarang.right is not None:
            node_sekarang = node_sekarang.right
        return node_sekarang.id_buku

    #Hitung tinggi tree (Height)
    def height(self):
        return self._height_rekursif(self.root)

    def _height_rekursif(self, node):
        # Base case 
        if node is None:
            return -1
        
        tinggi_kiri = self._height_rekursif(node.left)
        tinggi_kanan = self._height_rekursif(node.right)
        
        #Ambil jalur yang paling panjang, lalu tambah 1
        if tinggi_kiri > tinggi_kanan:
            return tinggi_kiri + 1
        else:
            return tinggi_kanan + 1


print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print("=========================================")

katalog = BST()

katalog.insert(50, "Dasar Pemrograman")
katalog.insert(30, "Struktur Data")
katalog.insert(70, "Kecerdasan Buatan")
katalog.insert(20, "Matematika Diskrit")
katalog.insert(40, "Basis Data")
katalog.insert(60, "Jaringan Komputer")
katalog.insert(80, "Sistem Operasi")

print("\n[INFO] Koleksi Buku (In-Order Traversal):")

katalog.traversal_inorder()

print()

katalog.search(60)
katalog.search(100)

print()

print(f"[STATISTIK] ID Terkecil: {katalog.get_min()}")
print(f"[STATISTIK] ID Terbesar: {katalog.get_max()}")
print(f"[INFO] Tinggi (Height) Tree: {katalog.height()}")

print("=========================================")
print("Simulasi Selesai!")