# 211. Design Add and Search Words Data Structure
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
# Example:
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
import re
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={"*":"*"}

    # See Trie explanation for this
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curr=self.root
        for char in word:
            if char not in curr:
                curr[char]={}
            curr=curr[char]
        curr["*"]="*"


    # If the words were concrete the search is much easier,
    # but since word has . at each level we have to traverse at all possible
    # cases. This leads to Time complexity of O(N.26^M) for undefined word.
    # For defined words both add and search is O(M) where M is word length.
    # Space complexity O(1) for defined and O(M) for keeping recursion stack for undefined
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def search_rc(word,root):
            curr_node=root
            for index,char in enumerate(word):
                if char not in curr_node:
                    # This can be real case or the char is .
                    if char==".":
                        # Search in all possible paths of the curent_node
                        # which is a hashmap recursively
                        for each_elem in curr_node:
                            # Either we have reached end of map or we again look
                            # rcursively in rest of the word where the . is found.
                            if each_elem!="*" and search_rc(word[index+1:],curr_node[each_elem]):
                                return True
                    # Not matching or there could be a case where the
                    # . is put and there is no word .For eg: worddict[a], search a., so the . is put and there is no
                    # such word.So return False not in else but in any case if
                    return False
                else:
                    # We shift pointer to next
                    curr_node=curr_node[char]
            # We do this till we reach end of word
            return "*" in curr_node
        return search_rc(word,self.root)




# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("")
param_2 = obj.search("")

print(re.search("bad.","bad").group())




