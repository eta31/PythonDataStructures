filename = "file.txt"

with open(filename) as fn:
    content = fn.readlines()

content = [x.strip() for x in content]

print(content)
