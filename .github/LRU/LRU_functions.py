#def LruBitsUpdate (set)
##include <bits/stdc++.h>

class LRUCache:
    # store keys of cache

    # store references of key in cache


    # Declare the size
    def __init__(self, n):
        #instance fields found by C++ to Python Converter:
        self._dq = []
        self._ma = {}
        self._csize = 0

        self._csize = n


    # Refers key x with in the LRU cache
    def refer(self, x):
        # not present in cache
        if x not in self._ma.keys():
            # cache is full
            if len(self._dq) == self._csize:
                # delete least recently used element
                last = self._dq[len(self._dq) - 1]

                # Pops the last element
                self._dq.pop(len(self._dq) - 1)

                # Erase the last
                self._ma.pop(last)

        # present in cache
        else:
#C++ TO PYTHON CONVERTER TODO TASK: There is no direct equivalent to the STL vector 'erase' method in Python:
            self._dq.erase(self._ma[x])

        # update reference
        self._dq.push_front(x)
        self._ma[x] = self._dq.begin()


    # Function to display contents of cache
    def display(self):

        # Iterate in the deque and print
        # all the elements in it
        for it in self._dq:
            print((*it), end = '')
            print(" ", end = '')

        print("\n", end = '')

# Driver Code
def main():
    ca = LRUCache(4)

    ca.refer(1)
    ca.refer(2)
    ca.refer(3)
    ca.refer(1)
    ca.refer(4)
    ca.refer(5)
    ca.display()

# This code is contributed by Satish Srinivas

if __name__ == "__main__":
    main()
