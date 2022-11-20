#sorted array to bst
'''
The idea is to find the middle element of the array and make it the root of the tree,
then perform the same operation on the left subarray for the roots left child and the same operation on the
right subarray for the roots right child.

Follow the steps mentioned below to implement the approach:

1.Set The middle element of the array as root.
2.Recursively do the same for the left half and right half.
3.Get the middle of the left half and make it the left child of the root created in step 1.
4.Get the middle of the right half and make it the right child of the root created in step 1.
5.Print the preorder of the tree. '''

# binary tree node
class Node:
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None

# function to convert sorted array to abalanced BST
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):
	
	if not arr:
		return None

	# find middle index
	mid = (len(arr)) // 2
	
	# make the middle element the root
	root = Node(arr[mid])
	
	# left subtree of root has all values 
	root.left = sortedArrayToBST(arr[:mid])
	
	# right subtree of root has all values >arr[mid]
	root.right = sortedArrayToBST(arr[mid+1:])
	return root

# A utility function to print the preorder traversal of the BST
def preOrder(node):
	if not node:
		return
	
	print ( node.data)
	preOrder(node.left)
	preOrder(node.right)

#Deleting a node in BST
class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)

# A utility function to insert a new node with given key in BST
def insert(node, key):
    
# If the tree is empty return a new node
	if node is None:
		return Node(key)
# Otherwise recursive down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)
	return node


# Given a binary search treeand a key, this function  delete the key and returns the new root
def deleteNode(root, key):

	if root is None:
		return root

# Recursive calls for ancestors of node to be deleted
	if key < root.key:
		root.left = deleteNode(root.left, key)
		return root

	elif(key > root.key):
		root.right = deleteNode(root.right, key)
		return root

# If root node is a leaf node
	
	if root.left is None and root.right is None:
		return None

# If one of the children is empty

	if root.left is None:
		temp = root.right
		root = None
		return temp

	elif root.right is None:
		temp = root.left
		root = None
		return temp

# If both children exist

	succParent = root

# Find Successor

	succ = root.right

	while succ.left != None:
		succParent = succ
		succ = succ.left

	if succParent != root:
		succParent.left = succ.right
	else:
		succParent.right = succ.right

# Copy Successor Data to root

	root.key = succ.key

	return root

#  to remove a given element from an array

def deleteElement(arr,n,x):

# If x is last element, nothing to do
	if arr[n-1]==x:
		return n-1


# elements one position ahead.

	prev = arr[n-1]
	for i in range(n-2,1,-1):
		if arr[i]!=x:
			curr = arr[i]
			arr[i] = prev
			prev = curr

# If element was not found
	if i<0:
		return 0

	# Else move the next element in place of x
	arr[i] = prev
	return n-1

#space complexity of both structures
'''
1. deleting an element fom an array 
 space complexity is O(1)
    
2. deleting an node from BST
   The space complexity of a binary search tree is O(n)
   in both the average and the worst cases.'''