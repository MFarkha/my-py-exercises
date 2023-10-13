class HashTable():
    def __init__(self, size):
        self.size = size
        self.data = [None]*self.size
            
    def _hash(self, key: str):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size
        return hash

    def set(self, key: str, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data[address]

    def get(self, key: str):
        address = self._hash(key)
        if self.data[address]:
            for pair in self.data[address]:
                if pair[0] == key:
                    return pair[1] 
        return None
    
    def keys(self) -> list[str]:
        keysList = []
        for i in range(self.size):
            if self.data[i]:
                for pair in self.data[i]:
                    keysList.append(pair[0])
        return keysList

myHashTable = HashTable(500)
# print (myHashTable._hash('grapes'))
print (myHashTable.set('grapes', 10000))
print (myHashTable.set('apples', 54))
print (myHashTable.set('oranges', 2))

print (myHashTable.get('grapes'))

print (myHashTable.keys())

# First Recurring Character
#

def firstRecurringCharacter(myArray):
    myDict = dict()
    for v in myArray:
        if not v in myDict:
            myDict[v] = True
        else:
            return v
    return None

myArray1 = [2,5,1,2,3,5,1,2,4]

myArray2 = [2,1,1,2,3,5,1,2,4]

myArray3 = [2,3,4,5]

print("--------FIRST Recurring Character----")
print(firstRecurringCharacter(myArray1))
print(firstRecurringCharacter(myArray2))
print(firstRecurringCharacter(myArray3))

