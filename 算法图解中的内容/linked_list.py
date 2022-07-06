class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = Node('xxx', None)
node2 = Node('Zjx', node1)

print(node2)
print(node2.data)
print(node2.next)
