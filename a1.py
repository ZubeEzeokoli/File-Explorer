from pathlib import Path
inp = input()
def recurse(p):
    """recursively prints the contents of directories or files depending on what option is chossen"""
    if option[-1] == '-r':
        #Prints files and directories in specified directory recursively
        ctr = 0
        if ctr == 0:
            for obj in Path(p).iterdir():
                if obj.is_file():
                    print(obj)
                    ctr += 1
                else:
                    ctr = -1
        if ctr > 0 or ctr == -1:
            for obj in Path(p).iterdir():
                if obj.is_dir():
                    print(obj)
                    recurse(obj)
    elif option[-1] == '-f':
        #Prints files in specified directory recursively
        ctr = 0
        if ctr == 0:
            for obj in Path(p).iterdir():
                if obj.is_file():
                    print(obj)
                    ctr += 1
                else:
                    ctr = -1
        if ctr > 0 or ctr == -1:
            for obj in Path(p).iterdir():
                if obj.is_file():
                    if not Path(obj).exists():
                        print(obj)
                else:
                    recurse(obj)
    elif option[-1] == '-s':
        #Prints files with the same name as the name given in input recursively
        ctr = 0
        if ctr == 0:
            for obj in Path(p).iterdir():
                if obj.is_file() and obj.name == suffix:
                    print(obj)
                    ctr += 1
                else:
                    ctr = -1
        if ctr > 0 or ctr == -1:
            for obj in Path(p).iterdir():
                if obj.is_dir():
                    recurse(obj)
                elif obj.is_file() and obj.name == suffix:
                    if not Path(obj).exists():
                        print(obj)
    elif option[-1] == '-e':
        #Prints files with the same suffix as the suffix given in the input recursively
        ctr = 0
        if ctr == 0:
            for obj in Path(p).iterdir():
                if obj.is_file() and obj.suffix[1:] == suffix:
                    print(obj)
                    ctr += 1
                else:
                    ctr = -1
        if ctr > 0 or ctr == -1:
            for obj in Path(p).iterdir():
                if obj.is_dir():
                    recurse(obj)
                elif obj.is_file() and obj.suffix[1:] == suffix:
                    if not Path(obj).exists() and obj.suffix[1:]:
                        print(obj)
            
            
        

    
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
        p = inp[2:index-1]
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
                #Lists the contents of the user specified directory and performs output based on option and if user wants to recursively
                if len(option) > 1:
                    #Recursive call if option has more than 1 element in its list such as ['-r', '-f']
                    recurse(p)
                elif len(option) == 1 and option[-1] == '-r':
                    #Prints everything in the specified directory recursively
                    recurse(p)
                elif len(option) == 1:
                        if option[0] == '-f':
                            #Prints files in specified directory
                            for obj in Path(p).iterdir():
                                if obj.is_file():
                                    print(obj)
                        if option[0] == '-s':
                            #Prints files with the same name as the name given
                            for obj in Path(p).iterdir():
                                if obj.name == suffix:
                                    print(obj)
                        if option[0] == '-e':
                            #Prints files with the same suffix as the suffix given
                            for obj in Path(p).iterdir():
                                if obj.suffix[1:] == suffix:
                                    print(obj)
                elif len(option) == 0:
                    #If no option is given just prints everything in one directory that was specified
                    p = inp[2:]
                    for obj in Path(p).iterdir():
                        if obj.is_file():
                            print(obj)
                    for obj in Path(p).iterdir():
                        if obj.is_dir():
                            print(obj)
                else:
                    print('ERROR')
                    
                inp = input()
            elif inp[:1].upper() == 'C':
                #Creates a new file in the specified directory
                if option[-1] == '-n':
                    new_file = suffix + '.dsu'
                    p1 = Path(p) / new_file
                    if not p1.exists():
                        p1.touch()
                        print(p1)
                inp = input()
            elif inp[:1].upper() == 'D':
                #Deletes the file that is specified
                p = inp[2:]
                if p[-3:] == 'dsu':
                    Path(p).unlink()
                    print(p, 'DELETED')
                    inp = input()
                else:
                    print('ERROR')
                    inp = input()
            elif inp[:1].upper() == 'R':
                #Reads the contents of a file that is specified
                p = inp[2:]
                if p[-3:] == 'dsu':
                    f = Path(p).open()
                    r = f.read()
                    if r == '':
                        print('EMPTY')
                        inp = input()
                    else:
                        print(r, end='')
                        inp = input()
                    f.close()
                else:
                    print('ERROR')
                    inp = input()
        else:
            print('ERROR')
            inp = input()
    else:
        print('ERROR')
        inp = input()
