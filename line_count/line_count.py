from sys import argv

script, filename = argv

print "I am going to open %r" % filename
target = open(filename)

print "I am going to count the number of lines in %s" % filename

counter = 0
for line in target:
    counter += 1

print counter
