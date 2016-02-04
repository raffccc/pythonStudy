#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them



def get_special_paths(directory):
    filenames = os.listdir(directory)
    
    paths = []
    for filename in filenames:
        if re.search('__\w+__', filename):
            absolutePath = os.path.abspath(os.path.join(directory, filename))
            paths.append(absolutePath)
    
    return paths

def copy_to(paths, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    for path in paths:
        shutil.copy(path, dir)
        
def zip_to(paths, zippath):
    commandToBeExecuted = 'zip -j ' + zippath + " " + " ".join(paths)
    print 'Command I will execute: ', commandToBeExecuted
    
    statusoutput = commands.getstatusoutput(commandToBeExecuted)
    if statusoutput[0]:
        sys.stderr.write(statusoutput[1])
        sys.exit(1)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)
    
    specialPaths = []
    for directory in args:
        dirPaths = get_special_paths(directory)
        for dirPath in dirPaths:
            if os.path.basename(dirPath) in [os.path.basename(specialpath) for specialpath in specialPaths]:
                sys.stderr.write('Duplicated File')
                sys.exit(1)
            specialPaths.append(dirPath)
        
    if todir:
        copy_to(specialPaths, todir)
        
    elif tozip:
        zip_to(specialPaths, tozip)
    else:
        print '\n'.join(specialPaths)
        
    
if __name__ == "__main__":
    main()
