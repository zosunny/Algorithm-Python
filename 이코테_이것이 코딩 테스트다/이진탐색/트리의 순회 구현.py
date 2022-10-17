class Node:
    def __init__(self, data, left_node, right_node):    #__init__ : 초기화를 위한 함수(메소드) = constructor
        self.data = data                                #self에는 인스턴스 자체가 전달되어 있음
        self.left_node = left_node
        self.right_node = right_node

#전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

#중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

#후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')

n = int(input())    #트리의 크기/노드의 개수
tree = {}           #딕셔너리

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":     #입력받은 문자열 'None'
        left_node = None        #None으로 선언
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)      #tree[data] : 인스턴스

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])