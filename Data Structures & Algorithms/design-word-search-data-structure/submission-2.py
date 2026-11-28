class PrefixNode:
    def __init__(self):
        self.children = {}
        self.is_eow = False

class WordDictionary:

    def __init__(self):
        self.root = PrefixNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in list(word):
            if c not in curr.children:
                curr.children[c] = PrefixNode()
            curr = curr.children[c]
        curr.is_eow = True
        
    def search(self, word: str) -> bool:
        def dfs(curr_idx, root):
            curr = root

            for i in range(curr_idx, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                
                else:
                    if c not in curr.children:
                        return False
                    
                    curr = curr.children[c]
            return curr.is_eow
        
        return dfs(0, self.root)
