from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def get_size(self):
        pass

class File(Node):
    def __init__(self, path, size):
        super().__init__(path)
        self.size = size

    def get_size(self):
        return self.size

class Directory(Node):
    def __init__(self, path):
        super().__init__(path)
        self.children = []
    
    def add_child(self, node):
        self.children.append(node)

    def get_size(self):
        return sum(child.get_size() for child in self.children)