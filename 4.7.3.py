def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('a')
buggy('b')
buggy('c')

def buggy(arg):
    result=[]
    result.append(arg)
    print(result)
buggy('a')
buggy('b')

def buggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
buggy('a')
buggy('b')