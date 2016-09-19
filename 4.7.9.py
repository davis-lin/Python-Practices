def knight2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knight2('Duck')
b = knight2('Hasenpfeffer')

print(type(a))
print(type(b))

print(a)
print(b)

print(a())
print(b())