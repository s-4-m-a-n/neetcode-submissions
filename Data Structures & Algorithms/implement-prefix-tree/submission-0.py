class PrefixNode:
    def __init__(self):
        self.children  = {}
        self.end_of_word = False


class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in list(word):
            if not c in node.children:
                node.children[c] = PrefixNode()
            node = node.children[c]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in list(word):
            if not c in node.children:
                return False
            node = node.children[c]
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in list(prefix):
            if not c in node.children:
                return False
            node = node.children[c]
        return True
        