class Node:

    def __init__(self, value: int):
        self.value = value
        self.left: Node = None
        self.right: Node = None 


class BinarySearchTree:
    
    def __init__(self):
        self.root: Node = None
        self.size = 0

    def insert(self, value: int) -> None:
        '''Inserts a number into the tree'''
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Node, value: int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)


    def search(self, value: int) -> bool:
        '''Returns whether or not a value is in the tree'''
        num = self.root
        while num != None:
            if value == num.value:
                return True
            elif value < num.value:
                num = num.left
            else:
                num = num.right
        return False
    

    def in_order_traversal(self) -> list[int]:
        '''returns a list of all the values'''
        tree_value = []
        list = []
        num = self.root

        while num or list:
            while num:
                list.append(num)
                num = num.left
            num = list.pop()
            tree_value.append(num.value)
            num = num.right
        return tree_value


    def find_min(self) -> int:
        '''returns the smallest number in the tree 
        (you cannot turn the tree into a list then return an element from the list, 
        you must do it by traversing the tree)'''
        min = self.root
        while min.left:
            min = min.left
        return min.value

    def find_max(self) -> int:
        '''returns the largest number in the tree 
        (you cannot turn the tree into a list then return an element from the list, 
        you must do it by traversing the tree)'''
        max = self.root
        while max.right:
            max = max.right
        return max.value


    def height(self) -> int: 
        '''returns the depth of the tree (how far is the furthest node from the root node?)'''
        max_height = 0
        num = [self.root]

        while num:
            next_level = []
            for node in num:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            max_height += 1
            num = next_level
        return max_height
    

    def count_leaves(self) -> int:
        '''returns the number of leaf nodes in the tree 
        (leaf nodes are nodes without any children)'''
        leaf_count = 0
        num = [self.root]

        while num:
            next_level = []
            for node in num:
                if node.left == None and node.right == None:
                    leaf_count += 1
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            num = next_level
        return leaf_count

    def serialize(self) -> str:
        '''turn the BST into a string'''
        result = []
        list = [self.root]
        while list:
            node = list.pop()
            if node:
                result.append(str(node.value))
                list.append(node.right)
                list.append(node.left)
        return ",".join(result)


    def deserialize(self, tree: str) -> None:
        """Deserialize a serialized BST.
        Take a string version of a BST and make an empty BST filled with those values.
        The new tree should match the tree that was serialized.
        """
        if not tree:
            self.root = None
            return
        values = tree.split(',')





def main():
    bst = BinarySearchTree()

    bst.insert(10)
    bst.insert(7)
    bst.insert(16)
    bst.insert(3)
    bst.insert(8)

    print()
    print("*** SEARCH ***")
    print(bst.search(3))

    print()
    print("*** IN ORDER ***")
    print(bst.in_order_traversal())

    print()
    print("*** MINIMUM ***")
    print(bst.find_min())

    print()
    print("*** MAXIMUM **")
    print(bst.find_max())

    print()
    print("*** HEIGHT ***")
    print(bst.height())

    print()
    print("*** TOTAL LEAVES ***")
    print(bst.count_leaves())

    print()
    print("*** SERIALIZE ***")
    print(bst.serialize())

    print()
    print("*** DESERIALIZE ***")
    tree = "10,7,3,8,16"
    print(bst.deserialize(tree))

if __name__ == "__main__":
    main()