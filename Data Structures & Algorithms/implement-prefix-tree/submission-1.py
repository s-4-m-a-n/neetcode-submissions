class PrefixNode:
    def __init__(self):
        self.children = {}
        self.is_eow = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in list(word):
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = PrefixNode()
                curr = curr.children[c]
        curr.is_eow = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in list(word):
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.is_eow

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in list(prefix):
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        