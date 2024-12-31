def output_values(x, y):
    for sult in range(x, y + 1):
        print(sult, end='')

numberA = int(input())
numberB = int(input())

print('Testing static input: ')
output_values(2, 6)
print(f'\nTesting user input: ')
output_values(numberA, numberB)