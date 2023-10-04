class MyHashMap:

    def __init__(self):
        self.hm = []
        
    def put(self, key: int, value: int) -> None:
        whereToPut = key
        for i in range(len(self.hm)):
            if(self.hm[i][0]==whereToPut):
                self.hm[i][1] = value
                return
        self.hm.append([whereToPut,value])
    def get(self, key: int) -> int:
        for i in range(len(self.hm)):
            if(self.hm[i][0] == key):
                return self.hm[i][1]
        return -1
    def remove(self, key: int) -> None:
        for i in range(len(self.hm)):
            # print(self.hm,i)
            if(self.hm[i][0] == key):
                if(i!=len(self.hm)-1):
                    self.hm = self.hm[0:i]+self.hm[i+1:]
                    return
                else:
                    self.hm = self.hm[:-1]
                    return
            

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)