import sys
# comment 

'''
multi-line comment

num = raw_input('What is your fave float? ')

print float(num) + 1

with open('numbers.txt', 'rb') as file:
	for line in file.readlines():
		print line.rstrip()


print('automatically prints newline')
#print 'doesnt print newline because of comma',

# how to do no newline with print() in python 3
print('lets print \'double quotes\'',end='\t')



sys.stdout.write('no newline either')
print('some more stuff')
'''

with open('numbers.txt', 'a') as file:
	file.write('\n42')