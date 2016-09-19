print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)
print('%d%%' % 42)

actor = 'Richard Gere'
cat = 'Chester'
weight = 28

print("My wife's favorite actor is %s" % actor)
print("Our cat %s weights %s pounds" % (cat, weight))

n = 42
f = 7.03
s = 'string cheese'

print('%d %f %s' % (n, f, s))
print('%10d %10f %10s' % (n, f, s))
print('%-10d %-10f %-10s' % (n, f, s))
print('%10.4d %10.4f %10.4s' % (n, f, s))

print('\n>>>>> Separate Line <<<<<\n')

print('{} {} {}'.format(n, f, s))
print('{2} {0} {1}'.format(n, f, s))
print('{n} {f} {s}'.format(n=42, f=7.03, s='string cheese'))

d = {'n': 42, 'f': 7.03, 's': 'string cheese'}

print('{0[n]}  {0[f]} {0[s]} {1}'.format(d, 'other'))
print('{0:d} {1:f} {2:s}'.format(n, f, s))
print('{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese'))