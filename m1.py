from pathlib import Path
def recurse(p, option, suffix):
    """recursively prints the contents of directories or files depending on what option is chossen"""
    if option[-1] == '-r':
        #Prints files and directories in specified directory recursively
        ctr = print_file(p)
        if ctr > 0 or ctr == -1:
            for obj in sorted(Path(p).iterdir()):
                if obj.is_dir():
                    print(obj)
                    recurse(obj, option, suffix)
    elif option[-1] == '-f':
        #Prints files in specified directory recursively
        ctr = print_file(p)
        if ctr > 0 or ctr == -1:
            for obj in sorted(Path(p).iterdir()):
                if obj.is_file():
                    if not Path(obj).exists():
                        print(obj)
                else:
                    recurse(obj, option, suffix)
    elif option[-1] == '-s':
        #Prints files with the same name as the name given in input recursively
        ctr = 0
        if ctr == 0:
            for obj in sorted(Path(p).iterdir()):
                if obj.is_file() and obj.name == suffix:
                    print(obj)
                    ctr += 1
                else:
                    ctr = -1
        if ctr > 0 or ctr == -1:
            for obj in sorted(Path(p).iterdir()):
                if obj.is_dir():
                    recurse(obj, option, suffix)
                elif obj.is_file() and obj.name == suffix:
                    if not Path(obj).exists():
                        print(obj)
    elif option[-1] == '-e':
        #Prints files with the same suffix as the suffix given in the input recursively
        ctr = 0
        if ctr == 0:
            for obj in sorted(Path(p).iterdir()):
                if obj.is_file() and obj.suffix[1:] == suffix:
                    print(obj)
                    ctr += 1
                else:
                    ctr = -1
        if ctr > 0 or ctr == -1:
            for obj in sorted(Path(p).iterdir()):
                if obj.is_dir():
                    recurse(obj, option, suffix)
                elif obj.is_file() and obj.suffix[1:] == suffix:
                    if not Path(obj).exists() and obj.suffix[1:]:
                        print(obj)

def print_file(p):
    #Prints files and directories in specified directory recursively
    ctr = 0
    if ctr == 0:
        for obj in sorted(Path(p).iterdir()):
            if obj.is_file():
                print(obj)
                ctr += 1
            else:
                ctr = -1
    return ctr

def look(option, extra, suffix, p, inp):
    '''Lists the contents of the user specified directory and performs output based on option and if user wants to recursively'''
    if len(option) > 1 or len(option) == 1 and extra[0] == '-r':
        #Recursive call if option has more than 1 element in its list such as ['-r', '-f'] or if it is only -r
        if len(extra) == 1 and extra[0] == '-r':
            recurse(p, option, suffix)
        elif extra[1] == '-f' or extra[1] == '-s' or extra[1] == '-e':
            recurse(p, option, suffix)
        else:
            print('ERROR')
    elif len(option) == 1:
            if option[0] == '-f':
                #Prints files in specified directory
                for obj in sorted(Path(p).iterdir()):
                    if obj.is_file():
                        print(obj)
            if option[0] == '-s':
                #Prints files with the same name as the name given
                    for obj in sorted(Path(p).iterdir()):
                        if obj.name == suffix:
                            print(obj)
            if option[0] == '-e':
                #Prints files with the same suffix as the suffix given
                for obj in sorted(Path(p).iterdir()):
                    if obj.suffix[1:] == suffix:
                        print(obj)
    elif len(option) == 0:
        #If no option is given just prints everything in one directory that was specified
        try:
            p = inp[2:]
            for obj in sorted(Path(p).iterdir()):
                if obj.is_file():
                    print(obj)
            for obj in sorted(Path(p).iterdir()):
                if obj.is_dir():
                    print(obj)
        except FileNotFoundError:
            print('ERROR')
    else:
        print('ERROR')

def create(option, suffix, p):
    '''Creates a new file in the specified directory'''
    if option[-1] == '-n':
        new_file = suffix + '.dsu'
        p1 = Path(p) / new_file
        if not p1.exists():
            p1.touch()
            print(p1)
    else:
        print('ERROR')

def delete(inp):
    '''Deletes the file that is specified'''
    p = inp[2:]
    if p[-3:] == 'dsu':
        Path(p).unlink()
        print(p, 'DELETED')
    else:
        print('ERROR')

def read(inp):
    '''Reads the contents of a file that is specified'''
    p = inp[2:]
    if p[-3:] == 'dsu':
        f = Path(p).open()
        r = f.read()
        if r == '':
            print('EMPTY')
        else:
            print(r, end='')
        f.close()
    else:
        print('ERROR')