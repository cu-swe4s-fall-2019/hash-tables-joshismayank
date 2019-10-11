import hash_functions

class LinearProbe:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        pass

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        pass

class ChainedHash:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        pass

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        pass


