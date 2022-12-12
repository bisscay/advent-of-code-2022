#!/usr/bin/python3
"""Template.py
    Author: Bissallah Ekele - bAe
    Date: 09/12/2022
    Description: Full Disk
"""
# filesystem - tree of files (plain data) | directories
# $ - commands you execute
# 
# total size (direct or indirect)
# directory has no intrinsic size
#
# sum(dir_size < = 100000)
# files can be counted more than once
#
# Pseudocode
# create filesystem tree with size and type in each node - type = (dir | file); size = 0
# BFS, if size <= 100000, increase total by size
#  
# if leaves sum up to size <= 100000, append parent-size tupil to list
# return sum(size) in parent-tupil list 

def get_dir_map(input_list):
    pwd = None
    ls_flag = False
    dir_map = {}
    for entry in input_list:
        if "$ cd " in entry:
            ls_flag = False
            _, _, pwd = entry.split(" ")

        if "$ ls" == entry:
            ls_flag = True

        if ls_flag and "$ ls" != entry:
            if pwd in dir_map:
                dir_map[pwd].append(entry)
            else:
                dir_map[pwd] = [entry,]
        
    return dir_map

class Node:
    # Pass in attributes of a new-node and it's parent-node
    # Create a new-node with parent-aware children-nodes
    # Show new-node it's parent
    # Show parent-node the new-node, parent's child

    def __init__(self, node_name=None, file_type=None, size=0, parent=None, children=None):
        self.node_name = node_name
        self.file_type = file_type
        self.size = size
        self.parent = parent
        self.children = children

        # Assign new-node previous to last-node
        self.parent = parent

        # Create set of parent aware child-node
        if children != None:
            self.children = set()
            for child in children:
                flag, name = child.split(" ")
                size = 0 if flag == "dir" else int(flag)
                file_type = "dir" if flag == "dir" else "file"
                child_node = Node(name, file_type, size)
                child_node.parent = self
                self.children.add(child_node)

        # Reassign last-node next to new element
        if parent != None:
            if parent.children != None:
                parent.children.add(self)
    
    def __repr__(self):
        """Node string representation."""
        return f"Node({self.file_type}:{self.node_name}:{self.size}, {self.children})"
        

class FileSystemTree:
    def __init__(self):
        self.root = None
        self.sum_under_100000 = 0

    def get_node(self, dir_name):
        # Get node with particular dir-name
        queue = [self.root]

        while queue:
            curr = queue.pop(0)

            if curr.node_name == dir_name:
                return curr
            
            if curr.children != None:
                for child in curr.children:
                    queue.append(child)
        
        return None          

    def add(self, dir_map):
        # Add dir-name to dir-content dict to tree
        for pwd in dir_map:
            if self.root == None:
                self.root = Node(pwd, "dir", 0, None, dir_map[pwd])
            else:
                # find node with same dir-name in current tree
                # place new-node after found node
                # remove old-node from parent
                found_node = self.get_node(pwd)
                Node(pwd, "dir", 0, found_node.parent, dir_map[pwd])
                found_node.parent.children.remove(found_node)
        return self.root
    
    def compute_dir_size(self, node):
        # PostOrder Traversal
        # find all dir
        # update node size with children size sum
        # keep count of dir-sums below 100000     
        if node.children != None and node.file_type == "dir":
            # Visit children
            for child in node.children:
                self.compute_dir_size(child)            
            # Visit yourself - node.visit()
            for child in node.children:
                node.size += child.size
            if node.size <= 100000:
                # print(node.node_name)
                self.sum_under_100000 += node.size

def get_part_1(input_list):
    tree = FileSystemTree()
    tree.add(get_dir_map(input_list))
    tree.compute_dir_size(tree.root)
    # print(tree.root)
    return tree.sum_under_100000

def get_part_2(input_list):
    """Function description

        Keyword argument:
        input_list -- parameter description

        Return:
        returned value

        Throws:
        if exceptions are thrown
    """
    pass

def main():
    test_input = r".\test-input"
    puzzle_input = "puzzle-input"

    file_name = puzzle_input #test_input

    with open(file_name) as f:
        input_list = f.read().splitlines()

    print("Part_1: " 
        + str(get_part_1(input_list)) 
        + "\nPart_2: "
        + str(get_part_2(input_list)))

if __name__ == "__main__":
    main()