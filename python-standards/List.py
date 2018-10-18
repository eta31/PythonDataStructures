# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item

list = ["Eta", '1994', 'Sainshand', 24]
print(list)
print(len(list))

print("{name} was born at {place} in {year}. Now he is {age}." .format(name=list[0], place=list[2], year=list[1], age=list[3]))

squares = [1, 3, 4, 6]
sum = 0
for x in squares:
    sum += x

print(sum)

if("Eta" in list):
    print('yay')

list.append("Dema")
list.extend(["Information about Dema", "1997", 'Uliastai', 20])
print(list)

list.insert(0, "Information about Eta")
print(list)
