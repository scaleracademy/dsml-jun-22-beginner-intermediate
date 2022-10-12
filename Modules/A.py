def add(a, b):
    return a + b

# is this module something you are running?
# NO, you are importing it

# __name__ == 'A'

if __name__ == '__main__':
    print(f'__name__ in A.py {__name__}')
