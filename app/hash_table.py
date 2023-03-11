from math import sqrt, gcd
from hash_entry import HashEntry


class HashTable:
    def __init__(self, ts):
        self.size = 0
        self.TABLE_SIZE = ts
        self.table = [None] * ts
        self.prime_size = self.get_prime()

    def __str__(self):
        s = ""
        for i in range(self.TABLE_SIZE):
            if self.table[i] is not None:
                # print(self._table[i].key, self._table[i].value)
                # s += f"({self.table[i].key}, {self.table[i].value})\n"
                s += f"(i={i} {self.table[i].key}, {self.table[i].value})"
        return s

    def get_prime(self):
        """Function to get a prime number less than table size."""
        for i in range(self.TABLE_SIZE - 1, 0, -1):
            fact = False
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    fact = True
                    break

            if not fact:
                return i

        return 3

    def remove(self, key):
        """Remove a key value pair from the hash table."""
        if self.size == 0:
            return

        hash1 = self.hash1(key)
        hash2 = self.hash2(hash1)

        while self.table[hash1] is not None and self.table[hash1].key != key:
            hash1 = (hash1 + hash2) % self.TABLE_SIZE

        self.table[hash1] = None
        self.size -= 1

    def insert(self, key, value):
        """Insert a key value pair into the hash table."""
        if self.size == self.TABLE_SIZE:
            raise RuntimeError("Table full!")
        h1 = self.hash1(key)
        h2 = self.hash2(h1)
        tries = 0
        while self.table[h1] is not None:
            h1 = (h1 + h2) % self.TABLE_SIZE
            tries += 1
            if tries > self.TABLE_SIZE:
                tries *= 1
        self.table[h1] = HashEntry(key, value)
        self.size += 1

    def my_hash(self, key_string):
        ascii_sum = 0
        for ch in key_string:
            ascii_sum += (ord(ch) - 96)
        return ascii_sum % self.TABLE_SIZE

    def hash1(self, s):
        """Create hash value for a string s."""
        # hash_val = hash(s) % self.TABLE_SIZE
        hash_val = self.my_hash(s)
        # return hash_val if hash_val >= 0 else hash_val + self.TABLE_SIZE
        # hash can yield -ve vals but % will always be +ve
        return hash_val % self.TABLE_SIZE

    def hash2(self, h1):
        """Create the second hash value based on the original hash. The original is calculated using hash1."""
        # return self.prime_size - h1 % self.prime_size
        return self.prime_size - (h1 % self.prime_size)


if __name__ == '__main__':
    import random
    from string import ascii_letters

    """The prime numbers from 1 to 200 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 
    197, 199."""
    # TABLE_SIZE = 10
    # KEY_SIZE = 3
    # VALUE_LEN = 10
    # RUNS = 1000
    # # ENTRIES_PER_RUN = 10
    #
    # for i in range(RUNS):
    #     hash_table = HashTable(TABLE_SIZE)
    #     # for j in range(ENTRIES_PER_RUN):
    #     for j in range(TABLE_SIZE):
    #         key_str = ''.join(random.sample(ascii_letters, KEY_SIZE))
    #         value_str = f'run={i}:entry{j} ' + ''.join(random.sample(ascii_letters, VALUE_LEN))
    #         hash_table.insert(key_str, value_str)
    # hash_table = HashTable(13)
    # hash_table.insert("John", "John Doe")
    # hash_table.insert("Jane", "Jane Doe")
    # hash_table.insert("Jasdne", "Jan466e Doe")
    # hash_table.insert("Jasdne", "Jane 4343Doe")
    # hash_table.insert("Jadsdne", "Ja34556ne Doe")
    # hash_table.insert("Jasdne", "Jan4433e Doe")
    # hash_table.insert("Jvvasdne", "Ja533466ne Doe")
    # hash_table.insert("Jsdcane", "Jane 43333oe")
    # hash_table.insert("Jandsfe", "Ja3566ne Doe")
    # hash_table.insert("assaJane", "Ja356567ne Doe")
    # hash_table.insert("Janfvcxve", "Ja4343543ne Doe")

    # print(hash_table)
    from math import gcd
    T_SIZE = 11
    hash_table = HashTable(T_SIZE)
    for i in range(T_SIZE):
        h2 = hash_table.hash2(i)
        print(f"i-{i} h2(i)={h2} i%7={i % 7} gcd({h2},{T_SIZE})={gcd(h2,T_SIZE)}")
        j = i
        for k in range(T_SIZE):
            print(f" {j}", end='')
            j = (j + h2) % T_SIZE
        print()
