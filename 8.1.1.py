poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

len(poem)

fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end=',')
fout.close()



try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists! That was a close one.')