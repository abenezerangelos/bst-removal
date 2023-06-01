words=['diaper','speed','sus','repaid','deeps']
def semordnilap(words):
    pairs=[]
    for i in words:
        j=list(reversed(list(i)))
        if ''.join(j) in words and i!=''.join(j) and words.index(i)<words.index(''.join(j)):
            pairs.append([i,''.join(j)])
    return pairs
def short(words):
    return ([[i,''.join(list(reversed(list(i))))] for i in words if ''.join(list(reversed(list(i)))) in words and i!=''.join(list(reversed(list(i)))) and words.index(i)<words.index(''.join(list(reversed(list(i)))))])
result=semordnilap(words)
ideal=short(words)
print(result)
print(ideal)
#####################################################
#BST validation
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# def levelOrderTraversal(root_array,double_array):
#     #returns a 2D array each array within our array will consist of all the nodes in one depth
#     print("Old/beginning array:",[w.value for w in root_array])
#     if not len(root_array):
#         return double_array
#     temp=[]
#     while len(root_array):
#         print("i:",root_array[0].value)
#         if root_array[0].left is not None:
#             print("Left",root_array[0].left.value)
#             temp.append(root_array[0].left)
#         if root_array[0].right is not None:
#             print("Right",root_array[0].right.value)
#             temp.append(root_array[0].right)
#         root_array.pop(0)
#     for j in temp:
#         root_array.append(j)
#         print("This",j.value)
#     print("New root_array:", [z.value for z in root_array])
#     if len(temp):
#         double_array.append([x.value for x in temp])
#     print("Double array in function:",double_array)
#     levelOrderTraversal(root_array,double_array)
def validate_right(right_node_array,focus):
    node = right_node_array[0]
    while len(right_node_array) and node is not None:
        node = right_node_array[0]
        node_value = right_node_array[0].value
        print("Node_value:", node_value)
        right_wing = node.right
        left_wing = node.left
        print("repetition:", [i.value for i in right_node_array])
        if node_value<focus:
            return False
        else:
            if right_wing is not None:
                right_node_array.append(right_wing)
            if left_wing is not None:
                right_node_array.append(left_wing)
        right_node_array.pop(0)
    return True




def validate_left(left_node_array,focus):
    node = left_node_array[0]
    while len(left_node_array) and node is not None:
        node = left_node_array[0]
        node_value = left_node_array[0].value
        right_wing = node.right
        left_wing = node.left
        print("repetition:",[i.value for i in left_node_array])
        if node_value>=focus:
            return False
        else:
            if left_wing is not None:
                left_node_array.append(left_wing)
            if right_wing is not None:
                left_node_array.append(right_wing)
        left_node_array.pop(0)
    return True
def validateBst(tree):
        if tree is None:
            return True
        truth1 = validateBst(tree.left)
        truth2 = validateBst(tree.right)

        reason=validate_left([tree.left], tree.value) and validate_right([tree.right],tree.value)


        ult_truth=truth1 and truth2 and reason
        print('Ult:',ult_truth)

        return ult_truth




root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

outcome=validateBst(root)
print(outcome)
array= [ 5,2,[7,-1],3,[6,[-13,8],4]]
def recurse(lister,counter):
    sum=0
    for i in lister:
        print(i)
        if isinstance(i,list):
            sum+=(counter+1)*recurse(i,counter+1)
        else:
            sum+=i
    return sum


def productSum(array):
    result=recurse(lister=array,counter=1)
    return result
productSum(array)





