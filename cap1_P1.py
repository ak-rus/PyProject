# Two pointer 

def TwoPoint(arr):
    l = res = 0
    r = len(arr)-1
    while l < r:
        # some condiition 
        if condition: 
            left += 1
        else:
            right -= 1
    return res

def TwoPointer(arr1, arr2):
    i, j, res = 0
    while i < len(arr1) and j < len(arr2):
        # some conditition to increase res 
        if condition:
            i += 1
        else:
            j ++ 1
    # exhaust arr1 
    while i < len(arr1):
        i += 1
    # exhaust arr2
    while j < len(arr2):
        j += 1
    return res
def TwoPointer(arr, i, j):
    res = 0
    while i < j:
        # some conditition to increase res 
        if condition:
            i += 1
        else:
            j -= 1
    return res

# Linkedlist 

# Doubly Linkedlist

# Reverse function
def reverseLinkedList(start, end):
    rev = None
    while start != end:
        rem = start.next
        start.next = rev
        rev = start
        start = rem
    return rev


# Binary Tree 

def dfs(root):
    if not root:
        return 
    
    res = 0
    # update res here
    dfs(root.left)
    dfs(root.right)
    return res

from collections import deque
def bfs(root):
    res = 0
    queue = deque([root])
    while queue:
        cur = queue.popleft()
        # update res
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return res


# Heaps
import heapq
def compute(arr, k):
    heap = []
    for num in arr:
        heapq.heappush(heap, (Criteria, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for num in heap]

# Binary Search
def binary_search(arr, target):
    l = 0
    r = len(arr)-1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return l # insertion point 

# Backtracking 
res = []
def backtrack(arr, pos, curr, n):
    if BASE_CASE:
        # add curr to res
        res.add(curr)
        return 
    for i in range(n):
        curr.append(arr[i])
        backtrack(arr, pos + 1, curr, n)
        curr.pop()
    return res

# Trie 
class TrieNode:
    def __init__(self):
        self.val = None
        self.children = {}
        self.isWord = False
def process(words):
    root = TrieNode()
    for word in words:
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
    return root

# 
