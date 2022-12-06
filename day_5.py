import re
from collections import deque

## part one
def p1(file):
    boxes, moves = file.read().split("\n\n")
    stacks = []

    for line in boxes.splitlines():
        for i, index in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            if line[index] != " ":
                stacks[i].append(line[index])

    for line1 in moves.splitlines():
        move, start, end = map(int, re.findall(r"\d+", line1))
        for i in range(move):
            stacks[end - 1].appendleft(stacks[start - 1].popleft())

    return "".join(x[0] for x in stacks)

file = open("crane.txt")
r = p1(file)
print(r)

### part 2


def p2(f):
    boxes, moves = file.read().split("\n\n")
    stacks = []

    for line in boxes.splitlines():
        for i, idx in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            if line[idx] != " ":
                stacks[i].append(line[idx])

    for line1 in moves.splitlines():
        move, start, end = map(int, re.findall(r"\d+", line1))
        temp = deque()
        for i in range(move):
            temp.appendleft(stacks[start - 1].popleft())
        stacks[end - 1].extendleft(temp)

    return "".join(x[0] for x in stacks)

file2 = open("crane.txt")
p = p2(file2)
print(p)

