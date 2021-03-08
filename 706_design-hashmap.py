# https://leetcode.com/problems/design-hashmap/
# 6gaksu

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.k = 1009
        self.buckets = [[] for i in range(0, self.k)]
        
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = self.buckets[key % self.k]
        item = next((item for item in bucket if item[0] == key), None)
        if item:
            item[1] = value
        else:
            bucket.append([key, value])
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = self.buckets[key % self.k]
        item = next((item for item in bucket if item[0] == key), None)
        if item:
            return item[1]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = self.buckets[key % self.k]
        item = next((item for item in bucket if item[0] == key), None)
        if item:
            bucket.remove(item)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)