# simple expression evaluator in python

operators = ["/", "*", "+", "-"]
punctuation = ["(", ")", *operators]

def split(s):
    strings = s.split(" ")
    i = 0
    while i < len(strings):
        t = strings[i]
        strings[i] = ""
        for j in range(len(t)):
            if t[j] in punctuation:
                strings.insert(i+1, t[j])
                strings.insert(i+2, "")
                i += 2
            else:
                strings[i] += t[j]
        i += 1
    while True:
        try:
            strings.remove("")
        except:
            break
    i = 1
    while i < len(strings):
        if strings[i] == "-" and strings[i-1] in operators:
            strings[i+1] = "-" + strings[i+1]
            del(strings[i])
            i -= 1
        i += 1
    return strings

def appNum(arr, n):
    if n == "!":
        return arr
    try:
        arr.append(float(n))
    except:
        printf("non number error")
        arr.append(0)
    return arr

def evalArr(arr):
    depth = 0
    start = 0
    i = 0
    while i < len(arr):
        if arr[i] == "(":
            if depth == 0:
                start = i
            depth += 1
        if arr[i] == ")":
            depth -= 1
            if depth == 0:
                a = arr[start+1:i]
                del(arr[start:i+1])
                arr.insert(start, evalArr(a))
        i += 1
    if depth != 0:
        print("brace error")
        return 0

    arr.insert(0, "!")
    arr.append("!")
    num = []
    ops = []
    for o in operators:
        for i in range(len(arr)):
            if arr[i] == o:
                ops.append(arr[i])
                num = appNum(num, arr[i-1])
                arr[i-1] = "!"
                num = appNum(num, arr[i+1])
                arr[i+1] = "!"
    if len(ops) != len(num)-1:
        print("error")
        return 0

    for o in ops:
        if o == "+":
            num[0] += num[1]
        if o == "-":
            num[0] -= num[1]
        if o == "*":
            num[0] *= num[1]
        if o == "/":
            if num[1] == 0:
                print("no")
            else:
                num[0] /= num[1]
        del(num[1])

    return num[0]

print("expression evaluator - tdwsl 2022")
print("blank line to quit")

while True:
    line = input()
    if line == "":
        break
    r = evalArr(split(line))
    if int(r) == r:
        r = int(r)
    print(r)

print("bye!")
