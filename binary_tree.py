class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        #A sebagai Root
        self.root = Node('A')
        
        #Anak dari A adalah B (kiri) dan C (kanan)
        self.root.left = Node('B')
        self.root.right = Node('C')
        
        #Anak dari B adalah D (kiri) dan E (kanan)
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        
        #Anak dari C hanya F di kanan (kirinya kosong)
        self.root.right.right = Node('F')

    #Traversal Pre-Order (Root -> Kiri -> Kanan)
    def traverse_preorder(self, node, hasil=None):
        if hasil is None:
            hasil = []
            
        if node is not None:
            hasil.append(node.data) #Kunjungi Root
            self.traverse_preorder(node.left, hasil) #Ke Kiri
            self.traverse_preorder(node.right, hasil) #Ke Kanan
            
        return hasil

    #Traversal In-Order (Kiri -> Root -> Kanan)
    def traverse_inorder(self, node, hasil=None):
        if hasil is None:
            hasil = []
            
        if node is not None:
            self.traverse_inorder(node.left, hasil) #Ke Kiri
            hasil.append(node.data) #Kunjungi Root
            self.traverse_inorder(node.right, hasil) #Ke Kanan
            
        return hasil

    #Traversal Post-Order (Kiri -> Kanan -> Root)
    def traverse_postorder(self, node, hasil=None):
        if hasil is None:
            hasil = []
            
        if node is not None:
            self.traverse_postorder(node.left, hasil) #Ke Kiri
            self.traverse_postorder(node.right, hasil) #Ke Kanan
            hasil.append(node.data) #Kunjungi Root
            
        return hasil

    #Cari Nodes yang tidak punya anak
    def get_leaf_nodes(self, node, hasil=None):
        if hasil is None:
            hasil = []
            
        if node is not None:
            #Kalau kiri dan kanan kosong, berarti gudang ujung yang tidak punya cabang lagi
            if node.left is None and node.right is None:
                hasil.append(node.data)
            
            #Lanjut cari ke bawah
            self.get_leaf_nodes(node.left, hasil)
            self.get_leaf_nodes(node.right, hasil)
            
        return hasil


print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print('======================================')
print('[INFO] Membangun Struktur Gudang...')

pohon_gudang = BinaryTree()
pohon_gudang.insert_manual()

print('[INFO] Struktur berhasil dibuat.\n')
print('HASIL AUDIT:')

pre_order_result = pohon_gudang.traverse_preorder(pohon_gudang.root)
print('1. Pre-Order :', ' - '.join(pre_order_result))

in_order_result = pohon_gudang.traverse_inorder(pohon_gudang.root)
print('2. In-Order :', ' - '.join(in_order_result))

post_order_result = pohon_gudang.traverse_postorder(pohon_gudang.root)
print('3. Post-Order :', ' - '.join(post_order_result))

#Mencari dan print gudang ujung
leaf_nodes = pohon_gudang.get_leaf_nodes(pohon_gudang.root)
print('\n[DATA] Gudang Ujung (Leaf Nodes):', ', '.join(leaf_nodes))

print('======================================')
print('Selesai!')