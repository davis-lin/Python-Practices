import re

source = "Young Frankenstein"
m = re.match('You', source)
if m:
    print(m.group())

m = re.match('^You', source)
if m:
    print(m.group())

m = re.match('Frank', source)
if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.match('.*Frank', source)
if m:
    print(m.group())

# p.139

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.findall('n', source)
print(m)
print('Found', len(m), 'matches')

print('\n >>> Use split()\n')
m = re.split('n', source)
print(m)

print('\n >>> Use sub()\n')

m = re.sub('n', '?', source)
print(m)

import string
printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])

print(re.findall('\d', printable))
print(re.findall('\w', printable))


source = '''I wish I may, I wish I might... Have a dish of fish tonight.'''
print(re.findall('wish', source))
print(re.findall ('wish|fish', source))
print(re.findall('^wish', source))
print(re.findall('^I wish', source))
print(re.findall('fish$', source))
print(re.findall('fish tonight.$', source))
print(re.findall('fish tonight\.$', source))
print(re.findall('[wf]ish', source))
print(re.findall('[wsh]+', source))
print(re.findall('[wsh]', source))
print(re.findall('ght\W', source))
print(re.findall('I (?=wish)', source))