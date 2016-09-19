def print_args(*args):
    print('Positional argument tuple:', args)

print_args()
print_args(3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scraf', 'monocle', 'mustache wax')