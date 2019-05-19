Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
    It is essentially a queue so it is constant time or O(1)

2. What is the space complexity of your ring buffer's `append` function?
    The space complexity is also constant O(1) 

3. What is the runtime complexity of your ring buffer's `get` method?
    This is also O(1)

4. What is the space complexity of your ring buffer's `get` method?
    I think this is O(1) since we're just returning what's already in memory

5. What is the runtime complexity of the provided code in `names.py`?
    It uses two for loops so O(n) * O(n) or O(n^2)

6. What is the space complexity of the provided code in `names.py`?
    I think this would either be O(n^2) becuase of the two for loops or just O(n) if not.

7. What is the runtime complexity of your optimized code in `names.py`?
    It uses a single for loop so with a dictionary so O(n)
    
8. What is the space complexity of your optimized code in `names.py`?
    It is also linear space complexity O(n)