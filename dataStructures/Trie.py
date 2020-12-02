class Trie:
    def __init__(self):
        self.root={"*":"*"}

    def add_word(self,word):
        curr_node=self.root
        # For each charecter we see if that is present in
        # the map as key. If not we add this char as new key
        # in the same level of map.
        for char in word:
            if char not in curr_node:
                curr_node[char]={}
            # We move our pointer to the next map
            # which is value of outer map
            curr_node=curr_node[char]
        # When the word is finished we add * as end marker
        curr_node["*"]="*"

    # We search for each leter and go down.Whenever
    #     we don't find any letter we return false'
    def search(self,word):
        curr_node=self.root
        for char in word:
            if char not in curr_node:
                return False
            curr_node=curr_node[char]
        return "*" in curr_node


