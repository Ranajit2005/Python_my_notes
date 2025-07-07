# conditional_and_loops
x = 10
if x > 5:
    print("x is greater than 5")

if x % 2 == 0:
    print("Even")
else:
    print("Odd")



marks = 75
if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")



for i in range(5):
    print(i)




count = 0
while count < 5:
    print(count)
    count += 1




for i in range(5):
    if i == 3:
        break
    print(i)




for i in range(3):
    print(i)
else:
    print("Loop finished")




for i in range(2):
    for j in range(3):
        print(i, j)

names = ['A', 'B']
scores = [90, 80]
for name, score in zip(names, scores):
    print(name, score)
# zip is used to combine two or more iterables (like lists) into tuples, allowing you to iterate over them in parallel.
# Example of using zip
# with two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
for item in zipped:
    print(item) 
# Output: (1, 'a'), (2, 'b'), (3, 'c')



