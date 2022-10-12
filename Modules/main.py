import arithmetic

def calculate(number):
    print('Function called from main.py')
    return number - 2

print(calculate(1))
print(arithmetic.calculate(1))