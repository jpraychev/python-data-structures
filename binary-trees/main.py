import random

# The node class
class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

# t_root = Node(5)
# t_1 = Node(4)
# t_2 = Node(6)
# t_root.left = t_1
# t_root.right = t_2

# print(t_root.left)
# print(t_root.right)

class Tree():

    def __init__(self):
        self.root = None
        self.l_height = 0
        self.r_height = 0

    def add(self, data):

        # If tree is empty
        if self.root == None:
            self.root = Node(data)
        else:
            self._add(self.root, data)

    def _add(self, current_node, data):
        
        if data > current_node.data:
            if current_node.right == None:
                current_node.right = Node(data)
            else:
                self._add(current_node.right, data)
        elif data < current_node.data:
            if current_node.left == None:
                current_node.left = Node(data)
            else:
                self._add(current_node.left, data)
        else:
            print('We have such item') 

    def remove(self, data):
        pass

    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, current_node):
        if current_node.left == None:
            return current_node.data
        self.l_height += 1
        return self._find_min(current_node.left)

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, current_node):
        if current_node.right == None:
            return current_node.data
        self.r_height += 1
        return self._find_max(current_node.right)

    def left_height(self):
        self.find_min()
        return self.l_height

    def right_height(self):
        self.find_max()
        return self.r_height


tree = Tree()

tree.add(50)
tree.add(30) 
tree.add(20) 
tree.add(40) 
tree.add(70) 
tree.add(60) 
tree.add(80)
tree.add(90)
tree.add(100)
tree.add(110)
tree.add(35)

# for _ in range(1,10):
#     value = random.randint(1,6789)
#     tree.add(int(value))

# print(tree.find_max())
# print(tree.find_min())

print(tree.right_height())
print(tree.left_height())


