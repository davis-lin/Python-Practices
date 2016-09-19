fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    #print(fragment)
    if not fragment:
        break
    poem += fragment
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    #print(line)
    if not line:
        break
    poem += line
    #print(poem)
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
for line in fin:
    print(line)
    poem += line
    print(poem)

fin.close()
len(poem)