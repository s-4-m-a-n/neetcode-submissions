class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in list(word):
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        
        def dfs(node, word):
            for i in range(len(word)):
                c = word[i]
                if c == ".":
                    for child in node.children.values():
                        if dfs(child, word[i+1:]):
                            return True
                    return False
                else:
                    if not c in node.children:
                        return False
                    node = node.children[c]
            return node.end_of_word

        return dfs(node, word)
