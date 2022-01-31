# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nzubechi Ezeokoli
# nezeokol@uci.edu
# 56611321
from pathlib import Path
import m1

inp = input()
while inp[:1].upper() != 'Q':
    if (inp[:1].upper() == 'L' or inp[:1].upper() == 'C' or inp[:1].upper() == 'R' or inp[:1].upper() == 'D') and inp[:2].upper() != 'C:':
        #Error handles if a command was given, if not an error will be printed
        for i in range(len(inp)):#Gets index of the space after the option so I can split after input/path
            index = 0
            if inp[i:i+2] == '-r':
                index = i
                break
            if inp[i:i+2] == '-f':
                index = i
                break
            if inp[i:i+2] == '-s':
                index = i
                break
            if inp[i:i+2] == '-e':
                index = i
                break
            if inp[i:i+2] == '-n':
                index = i
                break
        cmd = inp[0:1]
        if index != 0:
            p = inp[2:index-1]
        else:
            p = inp[2:]
        extra = inp[index:].split()
        option = []
        suffix = ''
        if len(inp) != 1:
            #Error handles to see if more than a command was given
            for x in range(len(extra)-1):#Differenciates from the list 'extra' to make a list of options, give a single option, and give suffix a value if given
                if extra[x] == '-r' or extra[x] == '-n' or extra[x] == '-f' or extra[x] == '-s' or extra[x] == '-e':
                    option.append(extra[x])
                else:
                    suffix += extra[x] + " "
            if extra[-1] == '-r' or extra[-1] == '-n' or extra[-1] == '-f' or extra[-1] == '-s' or extra[-1] == '-e':
                option.append(extra[-1])
            else:
                suffix += extra[-1]
            if inp[:1].upper() == 'L':
                m1.look(option, extra, suffix, p, inp)
            elif inp[:1].upper() == 'C':
                m1.create(option, suffix, p)
            elif inp[:1].upper() == 'D':
                m1.delete(inp)
            elif inp[:1].upper() == 'R':
                m1.read(inp)
        else:
            print('ERROR')
    else:
        print('ERROR')
    inp = input()