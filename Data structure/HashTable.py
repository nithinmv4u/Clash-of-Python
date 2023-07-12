class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    
    def hash(self, key):
        return key % self.size
    
    def add(self, key, value):
        index = self.hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                break
            else:
                self.table[index].append([key, value])
    
    def get(self, key):
        index = self.hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        else:
            return None

ht = HashTable()
ht.add(10, "apple")
ht.add(20, "banana")
ht.add(30, "orange")
print(ht.get(10))  
print(ht.get(20))  
print(ht.get(30))  
print(ht.get(40))  
