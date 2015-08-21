__author__ = 'Dixit_Patel'

from Node import Node

node = Node()
rear = Node()
node.num = 10;
node.next = Node();
node.prev = ""
rear = node

node.next.num = 11;
node.next.next = ""
node.next.prev = node


print(node.next.num)
print("rear: ", rear.num)