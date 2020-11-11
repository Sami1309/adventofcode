from copy import deepcopy

def iter(ops, pos):
    opcode = int(ops[pos])
    pos1 = int(ops[pos+1])
    pos2 = int(ops[pos+2])
    pos3 = int(ops[pos+3])

    val1 = int(ops[pos1])
    val2 = int(ops[pos2])
    res = 0
    if (opcode == 1):
        res = val1 + val2
    elif(opcode == 2):
        res = val1*val2
    ops[pos3] = res

def my_function(ops, in1, in2):
    pos = 0
    ops[1] = in1
    ops[2] = in2
    print(ops)
    while(int(ops[pos]) != 99):
        iter(ops, pos)
        pos += 4
    print("Program halted")
    print("Value at position 0 is ", ops[0])
    return int(ops[0])

def inputloop():
    for x in range(0,100):
        for y in range(0,100):
            ops = original[:]
            in1 = x
            in2 = y
            print("Inputs for this run are ", x, " and ", y)
            output = my_function(ops, in1, in2)
            if (output == 19690720):
                print("correct inputs found")
                return (x, y)


filepath = 'input2.txt'
ops = []
original = []
with open(filepath) as fp:
    #print(fp.read())
    ops = fp.read().split(',')
    original = []
    original = ops[:]
    result = inputloop()
    print(result)
    


    

