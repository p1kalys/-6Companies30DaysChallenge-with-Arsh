from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = OrderedDict()
        self.maxsize = capacity

    def get(self, key: int) -> int:
        if key in self.mapping:
            val = self.mapping[key]
            self.mapping.pop(key)
            self.mapping[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping.pop(key)
            self.mapping[key] = value
            self.mapping[key] = value
            return None
        if len(self.mapping) == self.maxsize:
            self.mapping.popitem(last = False)
        self.mapping[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
