fin = open('bfile', 'rb')
fin.tell()
print(fin.seek(25))

bdata = fin.read()
print(len(bdata))
print(bdata[0])

fin = open('bfile', 'rb')
print(fin.seek(-1, 2))
fin.tell()

bdata = fin.read()
print(len(bdata))
print(bdata[0])

print(fin.seek(254, 0))
print(fin.tell())

print(fin.seek(1, 1))
print(fin.tell())