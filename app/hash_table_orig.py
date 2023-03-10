from math import sqrt
from hash_entry import HashEntry


class HashTable:
    def __init__(self, ts):
        # should not use __ for private vars
        # in this case, private vars not even necessary

        self.__size = 0
        self.__TABLE_SIZE = ts
        self.__table = [None] * ts
        self.__prime_size = self.__get_prime()

    def insert(self, key, value):
        """Insert a key value pair into the hash table
        """
        # one-liner docstrings should be on one line and end with .

        if self.__size == self.__TABLE_SIZE:
            raise RuntimeError("Table full!")

        # bad practice to use the same names for methods and local vars
        hash1 = self.__hash1(key)
        hash2 = self.__hash2(hash1)

        while self.__table[hash1] is not None:
            # this is where the infinite loop occurs if table size is not prime
            hash1 = (hash1 + hash2) % self.__TABLE_SIZE

        self.__table[hash1] = HashEntry(key, value)
        self.__size += 1
        # at this point, the load factor should be considered and the table extended if over threshold

    def remove(self, key):
        """Remove a key value pair from the hash table
        """
        if self.__size == 0:
            return

        hash1 = self.__hash1(key)
        hash2 = self.__hash2(hash1)

        while self.__table[hash1] is not None and self.__table[hash1].key != key:
            hash1 = (hash1 + hash2) % self.__TABLE_SIZE

        self.__table[hash1] = None  # should leave a tombstone to let this func or a search func (if it existed) know
                                    # to keep looking
        self.__size -= 1

    def __get_prime(self):
        """Function to get a prime number less than table size
        """
        # could import and use sympy.ntheory.generate.prevprime(n)
        for i in range(self.__TABLE_SIZE - 1, 0, -1):
            fact = False
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    fact = True
                    break

            if not fact:
                return i

        return 3

    def __hash1(self, s):
        """Create hash value for a string s
        """
        hash_val = hash(s) % self.__TABLE_SIZE
        # % operator only returns positive numbers, so next line should just return hash_val
        return hash_val if hash_val >= 0 else hash_val + self.__TABLE_SIZE

    def __hash2(self, h):
        """Create the second hash value based on the original hash

        The original is calculated using hash1
        """
        # next line should have () around h % self.__prime_size for clarity/readability
        return self.__prime_size - h % self.__prime_size

    def __str__(self):
        # should never have print in __str__
        s = ""
        for i in range(self.__TABLE_SIZE):
            if self.__table[i] is not None:
                # the next line would be simpler if HashEntry had a __str__ func
                print(self.__table[i].key, self.__table[i].value)

        return s  # s is always empty


if __name__ == '__main__':
    # when double hashing as this module is, the table size must be a prime number or an infinite loop can
    # occur when trying to resolve collisions.
    # When table size is not a prime, the 2nd hash value and the table size will have a greatest common divisor
    # greater than 1 causing empty slots to be missed when hopping searching for the next empty slot.
    # sympy.ntheory.generate.nextprime(n, ith=1)[source] will find the next prime
    hash_table = HashTable(10)
    # this is insufficient test data
    hash_table.insert("John", "John Doe")
    hash_table.insert("Jane", "Jane Doe")

    print(hash_table)
