# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/
#
# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#
#
# Example 1:
#
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

# For Practice do word_search
# https://leetcode.com/problems/word-search/
class Solution(object):

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie=self.form_trie_from_words(words)
        matched_words=[]
        row_len=len(board)
        col_num=len(board[0])

        # We call this backtracking only
        # if the initial word matches the any trie start word
        def backtracking(row,col,trie_node):
            # We take the current letter from board
            curr_letter=board[row][col]
            # This letter exists in trie hence we're here'
            curr_node=trie_node[curr_letter]
            # We check if we're at the end of the word'
            word=curr_node.pop("*",False)
            if word:
                matched_words.append(word)
            # We mark the board cell as visited
            board[row][col]="#"

            # Next for this word we check neighbours in board for
            # matching letters
            for curr_row,curr_col in [(-1,0),(0,1),(0,-1),(1,0)]:
                new_row,new_col=curr_row+row,curr_col+col
                if new_row<0 or new_row>=row_len or new_col<0 or new_col>-col_num:
                    continue
                if board[new_row][new_col] not in curr_node:
                    continue
                backtracking(new_row,new_col,curr_node)

            # We assign back after algo completion
            board[row][col]=curr_letter

            # !!!!!!!This line takes runtime from 5k millisecs to 8milli secs
            # Because after each iteration, it reduces the trie
            # so less to explore
            if not curr_node:
                trie_node.pop(curr_letter)


        for row in range(row_len):
            for col in range(col_num):
                # We start backtracking only when a letter is found in Trie
                if board[row][col] in trie:
                    backtracking(row,col,trie)

        return matched_words




    def form_trie_from_words(self,words):
        trie={}
        for word in words:
            node=trie
            for char in word:
                if char not in node:
                    node[char]={}
                node=node[char]
            # Denotes end of word
            # For this problem we keep the
            # actual word as value to *
            # so that we can fetch it when we reach the end !!!!!
            node["*"]=word
        return trie

# 79. Word Search
#
# Given an m x n board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
# Constraints:
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 200
# 1 <= word.length <= 103
# board and word consists only of lowercase and uppercase English letters.
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # We iterate thru the grid,
        # whenever we find 1st matching letter
        # we trigger dfs with backtracking
        row_len=len(board)
        col_len=len(board[0])
        for row in range(row_len):
            for col in range(col_len):
                # When we find first matching char we start backtracking
                if board[row][col]==word[0]:



                    def backtrack(row,col,is_visited,new_str):
                        # If the new string ==word we found match return true
                        if new_str==word:
                            return True
                        # If new string and word upto length
                        # of new string doesn' match we backtrack as that is
                        # wrong path'
                        if new_str!=word[:len(new_str)]:
                            return False
                        # We look in 4 directions for DFS
                        for i,j in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                            if i>-1 and j>-1 and i<row_len and j<col_len:
                                # If the cell is not visited
                                if (i,j) not in is_visited:
                                    # Mark current cell as visited
                                    is_visited.add((i,j))
                                    # We add one char to newStr and call backtrack
                                    is_found=backtrack(i,j,is_visited,new_str+board[i][j])
                                    # If we have found a right path we go out
                                    if is_found:
                                        return True
                                    # Else we mark current cell as not visited and continue our search
                                    is_visited.remove((i,j))
                        return False


                    # We call the backtrack with current cell and if it returns True
                    # we return True
                    is_match=backtrack(row,col,{(row,col)},word[0])
                    if is_match:
                        return True
        return False






s=Solution()
s.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"])