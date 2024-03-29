import sys

if len(sys.argv) < 3:                                    #1
	print "You need to specify two directories:"        #1
	print sys.argv[0], "<directory 1> <directory 2>"    #1
	sys.exit()                                          #1

directory1 = sys.argv[1]                                 #2
directory2 = sys.argv[2]                                 #2

print "Comparing:"
print directory1
print directory2


import os

for directory in [directory1, directory2]:
        if not os.access(directory, os.F_OK):
                print directory, "is not a valid directory!"
                sys.exit()

        print "Directory", directory
        for item in os.walk(directory):        #1
                print item
        print

test_dir = list(os.walk(directory1))[0]
test_path = os.path.join(
        test_dir[0],
        test_dir[2][0])
print test_path

