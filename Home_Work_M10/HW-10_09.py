from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        self.keys = []
        for key, val in self.data.items():
            print(f"Key: {key}")
            print(f"Value: {val}")
            if val == value:
               self.keys.append(key)
            else:
                print("nothing")
        
        print(self.keys)
        return self.keys