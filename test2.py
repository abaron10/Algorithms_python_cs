# class Solution:
#     def isAlienSorted(self, words, order):
#         orders = {}
#         validation = 7
#         for i ,item in enumerate(order):
#             orders[item] = i  
        
#         for i in range(1,len(words)):
#             validation = self.compareWords(words[i-1],words[i],orders)
#             if not validation:
#                 break
        
#         return validation
            
                
        
    
#     def compareWords(self,word1,word2,orders):
#         print("entro")
#         if len(word1) > len(word2):
#             return False
#         for i in range(len(word1)):
#             print(word1)
#             print(word2)
#             if orders[word1[i]] > orders[word2[i]]:
#                 print("hola")
#                 return False
#         return True

# lis = ["hello","leetcode"]
# order = "hlabcdefgijkmnopqrstuvwxyz"
# test = Solution().isAlienSorted(lis,order)

# # print(test)


# import math
# # Add any extra import statements you may need here


# class TreeNode: 
#   def __init__(self,key): 
#     self.left = None
#     self.right = None
#     self.val = key 

# # Add any helper functions you may need here


# def visible_nodes(root):
#   # Write your code here
  
#     count = []
#     iteration(root,count,root)
#     return count
    
# def iteration(root,count, orig):
#     if root is None:
#       return
#     if root.left == None and root.val < orig.val:
#       count.append(root.val)
#     if root.left == None and root.right == None  and root.val > orig.val:
#       count.append(root.val)
#     iteration(root.left, count , orig)
#     iteration(root.right, count, orig)    
    
  



# def height_tree(self,root):
#         # Calculate the height of a Node 1 + max(height(L)+height(R))
#         # Here we use post-order traversal - we go first to leaves
#         if root is None:
#             return -1
#         if root.leftNode is None and root.rightNode is None:
#             return 0
#         return 1 + max(self.height_tree(root.leftNode), self.height_tree(root.rightNode))






# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

# def printInteger(n):
#   print('[', n, ']', sep='', end='')

# test_case_number = 1

# def check(expected, output):
#   global test_case_number
#   result = False
#   if expected == output:
#     result = True
#   rightTick = '\u2713'
#   wrongTick = '\u2717'
#   if result:
#     print(rightTick, 'Test #', test_case_number, sep='')
#   else:
#     print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
#     printInteger(expected)
#     print(' Your output: ', end='')
#     printInteger(output)
#     print()
#   test_case_number += 1

# if __name__ == "__main__":
#   root_1 = TreeNode(8)
#   root_1.left = TreeNode(3)
#   root_1.right = TreeNode(10)
#   root_1.left.left = TreeNode(1)
#   root_1.left.right = TreeNode(6)
#   root_1.left.right.left = TreeNode(4)
#   root_1.left.right.right = TreeNode(7)
#   root_1.right.right = TreeNode(14)
#   root_1.right.right.left = TreeNode(13)
#   expected_1 = 4
#   output_1 = visible_nodes(root_1)
#   check(expected_1, output_1)

#   root_2 = TreeNode(10)
#   root_2.left = TreeNode(8)
#   root_2.right = TreeNode(15)
#   root_2.left.left = TreeNode(4)
#   root_2.left.left.right = TreeNode(5)
#   root_2.left.left.right.right = TreeNode(6)
#   root_2.right.left =TreeNode(14)
#   root_2.right.right = TreeNode(16)

#   expected_2 = 5
#   output_2 = visible_nodes(root_2)
#   check(expected_2, output_2)

#   # Add your own test cases here




# def numPairsDivisibleBy60(time):
    
#   start, pairs = 0 , 0
#   for i in range(0,len(time)):
#     start = i + 1
#     while start < len(time):
#       target = (time[i] + time[start]) % 60
#       if target == 0:
#         pairs += 1
#       start += 1
#   return pairs

# print(numPairsDivisibleBy60([30,20,150,100,40]))
# print(30%60)


# def findCircleNum(nums):
#   count = 0
  
#   def dfs(nums, visited, i):
#       for j in range(len(nums[0])):
#           if nums[i][j] == 1 and not visited[j]:
#               visited[j] = 1
#               dfs(nums, visited, j)
      
  
#   visited = [0]*len(nums)
#   count = 0
  
#   for i in range(len(nums)):
#       if visited[i] == 0:
#           dfs(nums, visited, i)
#           count+=1
#   return count

# print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))

# from collections import defaultdict
# def findOrdernumCourses(prerequisites):
  
        
#   def topologicalSort(node,visited,stack):
#       if node in visited:
#           return
#       visited.add(node)
#       for n in rels[node]:
#         topologicalSort(n,visited,stack)
#       stack.append(node)
      
      
#   rels = {}
#   visited = set()
#   stack, response = [],[]
#   for pair in prerequisites:
#       if pair[1] not in rels:
#           rels[pair[1]],rels[pair[0]] = [],[]
#       rels[pair[1]].append(pair[0])
  
#   for course in sorted(rels):
#       topologicalSort(course,visited,stack)

#   while stack:
#     response.append(stack.pop())

#   return rels

# print(findOrdernumCourses([[0,1],[1,0]]))

def find(num):
  count = 0;
  while(num != 0):
    count += 1 if num % 10 == 1 else 0
    num /= 10;
  
  return count;

print(find(10101))