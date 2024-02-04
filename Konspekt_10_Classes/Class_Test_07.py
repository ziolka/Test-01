from collections import UserDict

class ValueSearchableDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values()
    
as_dict = ValueSearchableDict()
as_dict['a'] = 1
print(as_dict.has_in_values(1))
print(as_dict.has_in_values(2))




from collections import UserList

class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))
    
countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum())



from collections import UserString

class TruncatedString(UserString):
    MAX_LEN = 7
    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

ts = TruncatedString('1234567890')
ts.truncate()
print(ts)
