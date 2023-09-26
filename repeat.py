a = [10, 20, 30, 10, 20]
repeating_elements = []

for element in a:
    if a.count(element) > 1:
        if element not in repeating_elements:
           repeating_elements.append(element)

print(repeating_elements)
'''
a = [10, 20, 30, 10, 20]
b = []
for i in range(len(a)):
    if a[i] in b and a[i] not in b:
        b.append(i)
print(b)
'''