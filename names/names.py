import time
from heapq import merge 

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

def merge_lists(names_1, names_2):
    return list(merge(names_1, names_2))

if names_1 == names_2:
    duplicates = merge_lists(names_1, names_2)
print("Names", merge_lists(names_1, names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
