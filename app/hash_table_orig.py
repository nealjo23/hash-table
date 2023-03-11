from math import sqrt
from hash_entry import HashEntry


# John Neal 20003366
# 10/3/2023
# This hash-tables sample code from Blackboard uses double hashing.
# Double hashing is to resolve collisions - i.e. when the hashed key index is already filled.
# In this case, the 2nd hash value is an offset to add to the first index to look for an empty slot.
# If the new slot is filled, the offset is added again and again until an empty slot is found.
# At the end of the array, modulo division with the array size sets the index back to the start of the array.
#
# The problem with this example is that the array size is not a prime number.  This means it is possible for
# the 2nd hash value and the array size to have a common divisor > 1.  If this occurs when the hash table is not empty,
# the search for an empty slot can get into an infinite loop of looking at the same slots over and over without
# checking the empty slots.
# When table size is a prime, the 2nd hash value and the table size will have a greatest common divisor of 1, ensuring
# all slots are checked when hopping around searching for an empty slot.

# While researching this topic, I found that the algorithm in this code is __identical__ to the code
# shown on the following link:
#  https://www.topcoder.com/thrive/articles/double-hashing

# Other issues with this code are described within the code below.


class HashTable:
    def __init__(self, ts):
        # Should use _ not __ for private vars

        self.__size = 0
        self.__TABLE_SIZE = ts
        self.__table = [None] * ts
        self.__prime_size = self.__get_prime()

    def insert(self, key, value):
        """Insert a key value pair into the hash table
        """
        # One-liner docstrings should be on one line and end with . (https://peps.python.org/pep-0257/)

        if self.__size == self.__TABLE_SIZE:
            raise RuntimeError("Table full!")

        # Bad practice to use the same names for methods and local vars
        hash1 = self.__hash1(key)
        hash2 = self.__hash2(hash1)

        while self.__table[hash1] is not None:
            # This is where the infinite loop sometimes occurs if table size is not prime
            hash1 = (hash1 + hash2) % self.__TABLE_SIZE

        self.__table[hash1] = HashEntry(key, value)
        self.__size += 1
        # At this point, the load factor should be considered and the table extended if over some threshold.
        # Expand the table so the size is the next prime after double the current size

    def remove(self, key):
        """Remove a key value pair from the hash table
        """
        if self.__size == 0:
            return

        hash1 = self.__hash1(key)
        hash2 = self.__hash2(hash1)

        while self.__table[hash1] is not None and self.__table[hash1].key != key:
            hash1 = (hash1 + hash2) % self.__TABLE_SIZE

        # Should leave a tombstone to let this func (or a search func if it existed) know to keep looking next time
        self.__table[hash1] = None
        self.__size -= 1

    def __get_prime(self):
        """Function to get a prime number less than table size
        """
        # Could import and use sympy.ntheory.generate.prevprime(n) to find next prime number down
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
        # Modulo division on +ve value can only return +ve value, so condition is redundant - just return hash_val
        return hash_val if hash_val >= 0 else hash_val + self.__TABLE_SIZE

    def __hash2(self, h):
        """Create the second hash value based on the original hash

        The original is calculated using hash1
        """
        # Next line should have () around h % self.__prime_size for clarity/readability
        return self.__prime_size - h % self.__prime_size

    def __str__(self):
        s = ""
        for i in range(self.__TABLE_SIZE):
            if self.__table[i] is not None:
                # Should never use print in __str__
                # Also, would be simpler if HashEntry had a __str__ func
                # Should be s += f"{self.__table[i] } "
                print(self.__table[i].key, self.__table[i].value)

        return s


if __name__ == '__main__':
    # Hash table size should be prime.
    hash_table = HashTable(10)
    # To find the next prime after a given number, use sympy.ntheory.generate.nextprime(n)

    hash_table.insert("John", "John Doe")
    hash_table.insert("Jane", "Jane Doe")

    print(hash_table)
