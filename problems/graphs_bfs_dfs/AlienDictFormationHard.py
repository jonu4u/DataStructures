# 269. Alien Dictionary
# Hard
#
#
# Example 1:
#
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:
#
# Input: words = ["z","x"]
# Output: "zx"
# Example 3:
#
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.
from collections import deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Step 1: Create a hashmap to represent adjacency list for each charecter
        # and have an empty list as value. Map will be like {w:[],r:[]..} and so on. Each distinct letter is node
        graph={}
        for word in words:
            for char in word:
                graph[char]=[]
        # We have now the graph with distinct nodes and no relations
        indegree=[0]*26  # for 26 alphabets
        # Step 2: We find the relation between adjacent words
        sz=len(words)
        # We iterate till last -1th word
        for index in range(sz-1):
            word1=words[index]
            word2=words[index+1]
            len_min=min(len(word1),len(word2))
            # PREFIX CASE IMP!!!Let us handle the prefix case if one word is prefix of another
            #  Say ["abc","ab"].This is invalid
            if len(word1)>len(word2) and word1[:len_min]==word2:
                return ""

            # We iterate till length of smallest word
            for i in range(len_min):
                # Since dependency is from word1 to word2 so indegree
                # is calculated as to -> from(from has indegree, to has no idegree)
                from_char=word1[i]
                to_char=word2[i]
                # Whenever we have unequal we put dep in graph
                if to_char!=from_char:
                    graph[from_char].append(to_char)
                    # Get cell of corresponding char staring from 0 and add 1
                    indegree[ord(to_char)-ord('a')]+=1
                    break


        # Step 3: We do topological sort in our graph by doing BFS using queue
        q=deque()
        # We iterate over indegree and put 0 indegree in the q
        # for the charecter which exists in graph
        for index,elem in enumerate(indegree):
            if elem==0 and chr(ord('a')+index) in graph:
                q.append(chr(ord('a')+index))

        out_list=[]
        while len(q)>0:
            current=q.popleft()
            out_list.append(current)
            # Get the relations from the adjacency list and reduce indegree by 1.
            # If indegree is 0 put in q
            adj_list=graph[current]
            for node in adj_list:
                indegree_index=ord(node)-ord('a')
                indegree[indegree_index]-=1
                if indegree[indegree_index]==0:
                    q.append(node)
        out_string=''.join(out_list)
        return out_string if len(out_string)==len(graph) else ""

s=Solution()
print(s.alienOrder(["wrt","wrf","er","ett","rftt"]))
print(s.alienOrder(["z","x","z"]))







