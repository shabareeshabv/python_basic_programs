'''arr = [8, 5, 6, 7, 8, 99, 55, 33, 4, 5, 67]
d = {}

for element in arr:
    if element in d:
        d[element] += 1
    else:
        d[element] = 1

for element, count in d.items():
    print(f"Element: {element}, Frequency: {count}")'''
    
    
    
    #Python Program for sorting elements of an Array by Frequency
arr = [8, 5, 6, 7, 8, 99, 55, 33, 4, 5, 67]
d = {}

for element in arr:
    if element in d:
        d[element] += 1
    else:
        d[element] = 1

# Sort the dictionary by keys and create a new sorted dictionary
sorted_d = dict(sorted(d.items()))

for element, count in sorted_d.items():
    print(f"Element: {element}, Frequency: {count}")
