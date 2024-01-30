class WordDictionary:
    def __init__(self):
        self.data = set()

    def addWord(self, word: str) -> None:
        self.data.add(word)
        for i in range(len(word)):
            self.data.add(word[:i] + "." + word[i + 1 :])

    def search(self, word: str) -> bool:
        if word in self.data:
            return True
        if word.count(".") != 2:
            return False

        for c in "abcdefghijklmnopqrstuvwxyz":
            if word.replace(".", c, 1) in self.data:
                return True

        return False
