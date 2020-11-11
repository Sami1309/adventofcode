filepath = 'input.txt'
lines = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        lines.append(line)
        line = fp.readline()
print(len(lines))

total = 0

for n in lines:
    num = int(n)
    num = int(num/3)
    num = num - 2

    if(int(num/3) -2 > 0):
        test = int(num/3) -2
        while(test > 0):
            total += test
            test = int(test/3) - 2
    total = total + num

print(total)