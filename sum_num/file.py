file = open("input.txt")
data = file.read()
lines = data.split("\n")
total = 0
for line in lines:
    total = total + int(line)
print("sum:", total)