# Description: Day 1 Part 2 of Advent of Code

def solution(textfile: str) -> int:
    lines = textfile.split("\n")[:-1]

    fstlist = []
    sndlist = []

    for i in range(len(lines)): # split into two lists
        fst, snd = lines[i].split("  ")
        fstlist.append(int(fst))
        sndlist.append(int(snd))

    sndlist.sort()

    sum = 0

    for element in fstlist:
        sum += (element * sndlist.count(element))

    return sum
