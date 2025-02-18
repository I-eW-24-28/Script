# nodes.py

class Node:
    def __init__(self, value):
        self.value = value
        self.connections = {}
        
    def __str__(self):
        return f'Value: {self.value}\nNext: {self.next}'
        
    def set_next(self, next):
        self.connections['next'] = next