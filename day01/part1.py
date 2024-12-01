# Description: Day 1 Part 1 of Advent of Code


def solution(textfile: str) -> int:
    lines = textfile.split("\n")[:-1]

    fstlist = []
    sndlist = []

    for i in range(len(lines)): # split into two lists
        fst, snd = lines[i].split("  ")
        fstlist.append(int(fst))
        sndlist.append(int(snd))

    fstlist.sort()
    sndlist.sort()

    sum = 0

    for i in range(len(fstlist)):
        sum += abs(fstlist[i] - sndlist[i])

    return sum
