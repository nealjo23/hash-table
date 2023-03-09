from math import sqrt
from hash_entry import HashEntry


class HashTable:
    def __init__(self, ts):
        self.__size = 0
        self.__TABLE_SIZE = ts
        self.__table = [None] * ts
        self.__prime_size = self.__get_prime()

    def insert(self, key, value):
        """Insert a key value pair into the hash table
        """
        if self.__size == self.__TABLE_SIZE:
            raise RuntimeError("Table full!")

        hash1 = self.__hash1(key)
        hash2 = self.__hash2(hash1)

        while self.__table[hash1] is not None:
            hash1 = (hash1 + hash2) % self.__TABLE_SIZE

        self.__table[hash1] = HashEntry(key, value)
        self.__size += 1

    def remove(self, key):
        """Remove a key value pair from the hash table
        """
        if self.__size == 0:
            return

        hash1 = self.__hash1(key)
        hash2 = self.__hash2(hash1)

        while self.__table[hash1] is not None and self.__table[hash1].key != key:
            hash1 = (hash1 + hash2) % self.__TABLE_SIZE

        self.__table[hash1] = None
        self.__size -= 1

    def __get_prime(self):
        """Function to get a prime number less than table size
        """
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
        return hash_val if hash_val >= 0 else hash_val + self.__TABLE_SIZE

    def __hash2(self, h):
        """Create the second hash value based on the original hash

        The original is calculated using hash1
        """
        return self.__prime_size - h % self.__prime_size

    def __str__(self):
        s = ""
        for i in range(self.__TABLE_SIZE):
            if self.__table[i] is not None:
                print(self.__table[i].key, self.__table[i].value)

        return s


if __name__ == '__main__':
    hash_table = HashTable(10)
    hash_table.insert("John", "John Doe")
    hash_table.insert("Jane", "Jane Doe")
    hash_table.insert("Jasdne", "Jan466e Doe")
    hash_table.insert("Jasdne", "Jane 4343Doe")
    hash_table.insert("Jadsdne", "Ja34556ne Doe")
    hash_table.insert("Jasdne", "Jan4433e Doe")
    hash_table.insert("Jvvasdne", "Ja533466ne Doe")
    hash_table.insert("Jsdcane", "Jane 43333oe")
    hash_table.insert("Jandsfe", "Ja3566ne Doe")
    hash_table.insert("assaJane", "Ja356567ne Doe")
    hash_table.insert("Janfvcxve", "Ja4343543ne Doe")
    hash_table.insert("Jadsfdsfne", "Ja456477ne Doe")

    print(hash_table)
